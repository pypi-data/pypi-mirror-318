import asyncio
import os
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone

from boto3.session import Session

from aws_org_client.modules import identity_store, organizations, sso_admin
from aws_org_client.modules.logger import custom_logger

logger = custom_logger.get_logger(__name__)
PROFILE = os.environ["AWS_PROFILE"]


class Client:
    def __init__(self, identity_store_id: str, instance_arn: str, client_config=None):
        """Initialise client for organisation & identity services.

        Args:
            identity_store_id (str): The globally unique identifier for the identity store.
            instance_arn (str): The ARN of the IAM Identity Center instance under which the operation will be executed.
        """
        # [ TODO: load instance_arn & identity_store_id from local config ]
        # Input parameters
        self.identity_store_id = identity_store_id
        self.instance_arn = instance_arn
        self.client_config = client_config

        # Clients
        self.session = Session(profile_name=PROFILE, region_name="eu-west-2")
        self.idc_client = identity_store.IdentityStore(
            identity_store_id=self.identity_store_id, config=self.client_config
        )
        self.org_client = organizations.Organizations(config=self.client_config)
        self.sso_client = sso_admin.SSOAdmin(
            instance_arn=self.instance_arn, config=self.client_config
        )

        self.data = {}
        self.org_dict = {}

    async def bootstrap(self):
        """Use this method to query AWS for base data, including:
        * accounts
        * permission sets
        """
        get_accounts = asyncio.create_task(self.org_client.list_accounts())
        get_permission_sets = asyncio.create_task(
            self.sso_client.list_permission_sets()
        )

        await asyncio.gather(get_accounts, get_permission_sets)

        self.data["Accounts"] = get_accounts.result()
        self.data["PermissionSets"] = get_permission_sets.result()

    def construct_org_tree(self):
        try:
            with ThreadPoolExecutor(max_workers=16) as executor:
                futures = [
                    executor.submit(
                        self.construct_account_data,
                        account,
                    )
                    for account in self.data["Accounts"]
                ]
                pass
        except Exception as error:
            logger.error(error)

    def construct_account_data(self, account):
        logger.info(f"get account: {account['Name']}")
        account["PermissionSets"] = []
        account_id = account["Id"].strip()

        try:
            account_permissions = self.sso_client.list_account_permission_sets(
                account_id.strip()
            )
            logger.info(f"{len(account_permissions)} found for account: {account_id}")
        except Exception as error:
            logger.error(f"an error occured: {error}")

        for permission in account_permissions:
            account["PermissionSets"].append(permission)

        account_name = account["Name"]
        account.pop("JoinedMethod")
        account.pop("JoinedTimestamp")

        account["Groups"] = {}
        account["Users"] = {}

        ###
        # Permission Sets
        #
        # iterate all permission sets in account
        ###
        for permission_set in account["PermissionSets"]:
            logger.info(f"get permission set: {permission_set}")
            try:
                assignments = self.sso_client.list_account_assignments(
                    account_id, permission_set
                )
                logger.info(f"account permissions: {account_permissions}")
            except Exception as error:
                logger.error(f"an error occured: {error}")

            ###
            # Assignments
            # an account assignment is when a user, group entity is associated with an
            # account.
            ###
            for assignment in assignments:
                logger.info(
                    f"fetching assignment data: {assignment['PrincipalId']}, for: {account_id}"
                )
                ###
                # Groups
                # if the principal is group, construct group object
                # Returns:
                # "group_name": {
                #   "Id": group_id,
                #   "PermissionSets": [
                #     {
                #       "Name": permission_set_name,
                #       "Arn": permission_set,
                #       "Members": []
                #     }
                #   ]
                # }
                #
                ###
                if assignment["PrincipalType"] == "GROUP":
                    # [TODO: def group_assignment]
                    group_id = assignment["PrincipalId"]
                    logger.info(f"GROUP type assignment found: {group_id}")

                    group_data = self.idc_client.describe_group(group_id)
                    group_name = group_data["DisplayName"]
                    logger.info(f"constructing group data for: {group_name}")

                    # Check if account exist, otherwise initialise group object
                    if group_name in account["Groups"].keys():
                        # group exists, do nothing
                        logger.warning(f"group exists: {group_name}")
                        pass
                    else:
                        account["Groups"][group_name] = {
                            "Id": group_data["GroupId"],
                            "PermissionSets": [],
                            "Members": [],
                        }
                        logger.info(
                            f"adding group: {group_name}, to account: {account_id}"
                        )

                    group_id = account["Groups"][group_name]["Id"]
                    group_members = self.idc_client.list_group_memberships(group_id)
                    for member in group_members:
                        member_id = member["MemberId"]["UserId"]
                        member_data = self.idc_client.describe_user(member_id)

                        logger.info(
                            f"adding user: {member_data['UserName']}, to group members: {group_name}"
                        )
                        account["Groups"][group_name]["Members"].append(
                            {
                                "MembershipId": member["MembershipId"],
                                "UserId": member_data["UserId"],
                                "UserName": member_data["UserName"],
                            }
                        )

                    logger.info(
                        f"finished adding members for: {group_name} in: {account_id}"
                    )

                    if assignment["PermissionSetArn"] == permission_set:
                        permission_set_data = self.sso_client.describe_permission_set(
                            permission_set
                        )
                        permission_set_name = permission_set_data["Name"]
                        permssion_set_arn = permission_set_data["PermissionSetArn"]

                        ###
                        # Group Policies
                        ###
                        policies = {}
                        ###
                        ## Customer Managed Policies
                        logger.info(f"get customer managed policy...")
                        customer_policy_data = self.sso_client.list_customer_managed_policy_references_in_permission_set(
                            permssion_set_arn
                        )
                        logger.debug(customer_policy_data)

                        if customer_policy_data != []:
                            logger.info(f"customer managed policy present...")
                            policies["CustomerManaged"] = customer_policy_data
                        else:
                            logger.warning(f"customer managed policy is null...")
                            pass

                        ###
                        ## AWS Managed Policies
                        logger.info(f"get aws managed policy...")
                        managed_policy_data = (
                            self.sso_client.list_managed_policies_in_permission_set(
                                permssion_set_arn
                            )
                        )
                        managed_policies = []
                        for policy in managed_policy_data:
                            managed_policies.append(policy)
                        if managed_policies is not None:
                            logger.info(f"aws managed policy present...")
                            policies["AWSManaged"] = managed_policies
                        else:
                            logger.warning(f"customer managed policy is null...")
                            pass

                        ###
                        ## Inline Policies
                        logger.info(f"get inline policy...")
                        inline_policy_data = (
                            self.sso_client.get_inline_policy_for_permission_set(
                                permssion_set_arn
                            )
                        )
                        inline_policy_data.pop("ResponseMetadata")
                        if inline_policy_data["InlinePolicy"] != "":
                            logger.info(f"inline policy present...")
                            policies["Inline"] = inline_policy_data
                        else:
                            logger.warning(f"inline policy policy is null...")
                            pass

                        logger.info(f"constructing group policy object...")
                        policy_obj = {
                            "Name": permission_set_name,
                            "Arn": permission_set,
                            "Policies": policies,
                        }

                        account["Groups"][group_name]["PermissionSets"].append(
                            policy_obj
                        )
                    logger.info(f"finished GROUP assignment for: {group_id}")

                ###
                # Users
                # if the principal is users, construct users object
                # Returns:
                # user_name: {
                #   "Id": user_id,
                #     "PermissionSets": [
                #       {
                #         "Name": permission_set_name,
                #         "Arn": permission_set,
                #         "CustomerManagedPolicies": [],
                #         "AWSManagedPolicies": [
                #           {
                #             "Arn": "arn:aws:iam::aws:policy/AdministratorAccess",
                #             "Name": "AdministratorAccess"
                #           }
                #         ],
                #         "InlinePolicies": {
                #           'InlinePolicy': 'string'
                #         }
                #       }
                #   ]
                # }
                #
                ###
                elif assignment["PrincipalType"] == "USER":
                    # [TODO: def user_assignment]
                    user_id = assignment["PrincipalId"]
                    logger.info(f"USER type assignment found: {user_id}")

                    user_data = self.idc_client.describe_user(user_id)
                    user_name = user_data["UserName"]

                    # Check if user exist, otherwise add initialise object
                    if user_name in account["Users"].keys():
                        # user exists, do nothing
                        logger.warning(f"user exists: {user_name}")
                        pass
                    else:
                        account["Users"][user_name] = {"Id": user_data["UserId"]}
                        account["Users"][user_name]["PermissionSets"] = []
                        logger.info(f"Appending user to account...")

                    if assignment["PermissionSetArn"] == permission_set:
                        permission_set_data = self.sso_client.describe_permission_set(
                            permission_set
                        )

                        permission_set_name = permission_set_data["Name"]
                        permssion_set_arn = permission_set_data["PermissionSetArn"]

                        ###
                        # User Policies
                        ###
                        policies = {}
                        ###
                        ## Customer Managed Policies
                        logger.info(f"get customer managed policy...")
                        customer_policy_data = self.sso_client.list_customer_managed_policy_references_in_permission_set(
                            permssion_set_arn
                        )
                        logger.debug(customer_policy_data)

                        if customer_policy_data != []:
                            logger.info(f"customer managed policy present...")
                            policies["CustomerManaged"] = customer_policy_data
                        else:
                            logger.warning(f"customer managed policy is null...")
                            pass

                        ###
                        ## AWS Managed Policies
                        logger.info(f"get aws managed policy...")
                        managed_policy_data = (
                            self.sso_client.list_managed_policies_in_permission_set(
                                permssion_set_arn
                            )
                        )
                        managed_policies = []
                        for policy in managed_policy_data:
                            managed_policies.append(policy)
                        if managed_policies is not None:
                            logger.info(f"aws managed policy present...")
                            policies["AWSManaged"] = managed_policies
                        else:
                            logger.warning(f"customer managed policy is null...")
                            pass

                        ###
                        ## Inline Policies
                        logger.info(f"get inline policy...")
                        inline_policy_data = (
                            self.sso_client.get_inline_policy_for_permission_set(
                                permssion_set_arn
                            )
                        )
                        inline_policy_data.pop("ResponseMetadata")
                        if inline_policy_data["InlinePolicy"] != "":
                            logger.info(f"inline policy present...")
                            policies["Inline"] = inline_policy_data
                        else:
                            logger.warning(f"inline policy policy is null...")
                            pass

                        logger.info(f"constructing user policy object...")
                        policy_obj = {
                            "Name": permission_set_name,
                            "Arn": permission_set,
                            "Policies": policies,
                        }

                        account["Users"][user_name]["PermissionSets"].append(policy_obj)

                    logger.info(f"finished USER assignment for: {user_id}")

        logger.info(f"dropping account permission set key...")
        account.pop("PermissionSets")

        logger.info(f"updating org dict...")
        self.org_dict[account_name] = account

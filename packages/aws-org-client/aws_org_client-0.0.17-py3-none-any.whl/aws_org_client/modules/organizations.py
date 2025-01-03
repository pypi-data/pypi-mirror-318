import boto3
from botocore.exceptions import ClientError

from aws_org_client.modules.logger import custom_logger

logger = custom_logger.get_logger(__name__)


class Organizations:
    def __init__(self, config=None):
        logger.info("Init organizations client...")
        self.org_client = boto3.client("organizations", config=config)

    async def list_accounts(self):
        logger.info("Listing accounts...")
        accounts = []
        next_token = None

        # [TODO: use paginator]
        while True:
            if next_token:
                logger.info("Iterating through account pages...")
                response = self.org_client.list_accounts(NextToken=next_token)
            else:
                response = self.org_client.list_accounts()

            accounts.extend(response.get("Accounts", []))
            next_token = response.get("NextToken")

            if not next_token:
                break

        logger.info("Accounts listed...")
        return accounts

    def describe_account(self, account_id: str):
        """Provide detailed information regarding AWS account.

        Args:
            account_id (str): the id of the account to describe.

        Raises:
            error: botocore exceptions for organisations client errors.

        Returns:
            dict: describe account response.
        """
        logger.info(f"Describing account: {account_id}")

        try:
            response = self.org_client.describe_account(AccountId=account_id)

            return response.get("Account")

        except ClientError as error:
            logger.error(error)

            raise error

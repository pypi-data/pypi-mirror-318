import asyncio
import json
import os

import click
from botocore.config import Config

from aws_org_client.modules.logger import custom_logger

from .client import Client

logger = custom_logger.get_logger(__name__)


boto_client_config = Config(
    retries={
        "total_max_attempts": 10,
        "mode": "adaptive",
    }
)


# Init aws org client
client = Client(
    identity_store_id=os.environ["IDENTITY_STORE_ID"],
    instance_arn=os.environ["SSO_INSTANCE_ARN"],
    client_config=boto_client_config,
)


@click.group()
@click.version_option()
def cli():
    """AWS Org Client CLI, utility for browsing and modifying organisation, sso & idc resources."""


###
# Client commands
###
@cli.command("bootstrap")
def bootstrap():
    """construct org map."""
    if "Accounts" not in client.data.keys():
        logger.warning("data property empty, bootstrapping...")
        asyncio.run(client.bootstrap())
    else:
        logger.info("bootstrap data available, constructing org...")

    client.construct_org_tree()
    client.org_dict
    logger.info("writing bootstrap data to: org.json...")
    with open("org.json", "w") as file:
        file.write(json.dumps(client.org_dict))


@cli.command("list-memberships")
@click.option("-uid", "--user-id", "user_id")
def list_memberships(user_id):
    """expose group memberships for specific user."""

    matches = []

    with open("org.json") as json_file:
        data = json.load(json_file)
    if len(data.keys()) == 0:
        logger.warning("data property empty, bootstrapping...")
        asyncio.run(client.bootstrap())
    else:
        for account in data:
            for group in data[account]["Groups"]:
                print(data[account]["Groups"][group]["Members"])
                for member in data[account]["Groups"][group]["Members"]:
                    if member == user_id:
                        print(member)
                        matches.append(account, group, member)

    click.echo(matches)


###
# Org command group
###


@cli.group("org")
def org():
    """organisations related commands."""


@org.command("list")
def org_list():
    """list organisation accounts."""
    click.echo(client.accounts)


@org.command("describe")
@click.option("-id", "--account-id", "account_id")
def org_list(account_id):
    account_description = client.org_client.describe_account(account_id)
    click.echo(account_description)

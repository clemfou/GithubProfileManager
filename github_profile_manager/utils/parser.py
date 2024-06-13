"""Parse program's arguments."""

import argparse
from pathlib import Path

from github_profile_manager.keys import (
    add_ssh_key,
    list_ssh_key,
    remove_ssh_key,
)


def parse_args(args: list) -> argparse.Namespace:
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        prog="github-profile-manager",
        description="A tool I use to manage my github profile",
    )

    parser.add_argument(
        "--config",
        nargs="?",
        type=Path,
        default="/etc/clemfou/github_profile_manager.json",
    )
    subparsers = parser.add_subparsers()

    ssh_parser = subparsers.add_parser("ssh", help="manage my ssh keys")
    ssh_subparser = ssh_parser.add_subparsers()

    list_ssh_key_parser = ssh_subparser.add_parser("list", help="list my ssh keys")
    list_ssh_key_parser.set_defaults(func=list_ssh_key)

    add_ssh_key_parser = ssh_subparser.add_parser(
        "add",
        help="Add SSH key to my account",
    )
    add_ssh_key_parser.add_argument("name", type=str, help="key display name")
    add_ssh_key_parser.add_argument("key", type=str, help="ssh key to add")
    add_ssh_key_parser.set_defaults(func=add_ssh_key)

    del_ssh_key_parser = ssh_subparser.add_parser(
        "remove",
        help="Remove SSH key from my account",
    )
    del_ssh_key_parser.add_argument("key_id", type=str, help="ssh key id to remove")
    del_ssh_key_parser.set_defaults(func=remove_ssh_key)



    if not args:
        parser.print_help()

    return parser.parse_args(args)

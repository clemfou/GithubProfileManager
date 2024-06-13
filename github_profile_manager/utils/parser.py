"""Parse program's arguments."""

import argparse
from pathlib import Path

from github_profile_manager.keys import (
    add_ssh_key,
    list_ssh_key,
    remove_ssh_key,
)
from github_profile_manager.repositories import (
    create_repository,
    list_repositories,
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

    repository_parser = subparsers.add_parser("repo", help="manage my repositories")
    repository_subparser = repository_parser.add_subparsers()

    create_repository_parser = repository_subparser.add_parser("list", help="list my repositories")
    create_repository_parser.set_defaults(func=list_repositories)

    create_repository_parser = repository_subparser.add_parser("add", help="create a repository")
    create_repository_parser.add_argument("name", type=str, help="repository name")
    create_repository_parser.add_argument(
        "-d",
        "--description",
        type=str,
        metavar="description",
        help="short description",
    )
    create_repository_parser.add_argument(
        "--allow-squash-merge",
        action="store_true",
        default=True,
        help="wether to allow squash merge for pull requests",
    )
    create_repository_parser.add_argument(
        "--allow-merge-commit",
        action="store_true",
        default=True,
        help="wether to allow merge commits for pull requests",
    )
    create_repository_parser.add_argument(
        "--allow-rebase-merge",
        action="store_true",
        default=True,
        help="wether to allow rebase merges for pull requests",
    )
    create_repository_parser.add_argument(
        "--private",
        action="store_true",
        default=False,
        help="wether this repository is private",
    )
    create_repository_parser.add_argument(
        "--auto-init",
        action="store_true",
        default=False,
        help="wether this repository is created with a README",
    )
    create_repository_parser.add_argument(
        "--has-discussions",
        action="store_true",
        default=False,
        help="wether discussions are enabled",
    )
    create_repository_parser.add_argument(
        "--has-projects",
        action="store_true",
        default=True,
        help="wether projects are enabled",
    )
    create_repository_parser.add_argument(
        "--has-issues",
        action="store_true",
        default=True,
        help="wether issues are enabled",
    )
    create_repository_parser.add_argument(
        "--has-downloads",
        action="store_true",
        default=True,
        help="wether downloads are enabled",
    )
    create_repository_parser.add_argument(
        "--is-template",
        action="store_true",
        default=False,
        help="wether this repository acts as a template",
    )
    create_repository_parser.set_defaults(func=create_repository)

    if not args:
        parser.print_help()

    return parser.parse_args(args)

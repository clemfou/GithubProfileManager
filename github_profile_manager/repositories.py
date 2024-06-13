"""Manages my github account repositories."""

import pprint

from github_profile_manager import global_variables as globs


def list_repositories() -> None:
    """List repositories."""
    response = globs.GITHUB_API.get("user/repos")
    pprint.pp(response)


def create_repository(**kwargs: dict) -> None:
    """Create repository."""
    response = globs.GITHUB_API.post("user/repos", kwargs)
    pprint.pp(response)

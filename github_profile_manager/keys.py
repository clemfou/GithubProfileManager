"""Manages my github account ssh keys."""

import json

from github_profile_manager import global_variables as globs


def list_ssh_key() -> None:
    """List SSH keys encoded in my github account."""
    ssh_keys = globs.GITHUB_API.get("user/keys")
    print(json.dumps(ssh_keys, indent=4))  # noqa: T201


def remove_ssh_key(key_id: str) -> None:
    """Remove SSH key from the account."""
    endpoint = f"user/keys/{key_id}"

    globs.GITHUB_API.delete(endpoint)


def add_ssh_key(name: str, key: str) -> None:
    """Add SSH key from the account."""
    data = {"title": name, "key": key}
    response = globs.GITHUB_API.post("user/keys", data)

    globs.LOGGER.info("Added key %s with ID %s", name, response["id"])

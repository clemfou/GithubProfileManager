"""Manages the github account."""

import json

from github_profile_manager import global_variables as globs
from github_profile_manager.api import GithubAPI


class GithubAccount:
    """Manage my Github account."""

    def __init__(self) -> None:
        """Init the GithubAccount class."""
        self.api = GithubAPI(globs.CONFIG.api_config)

    def list_ssh_key(self) -> None:
        """List SSH keys encoded in my github account."""
        ssh_keys = self.api.get("user/keys")
        print(json.dumps(ssh_keys, indent=4))  # noqa: T201

    def remove_ssh_key(self, key_id: str) -> None:
        """Remove SSH key from the account."""
        endpoint = f"user/keys/{key_id}"

        self.api.delete(endpoint)

    def add_ssh_key(self, name: str, key: str) -> None:
        """Add SSH key from the account."""
        data = {"title": name, "key": key}
        response = self.api.post("user/keys", data)

        globs.LOGGER.info("Added key %s with ID %s", name, response["id"])

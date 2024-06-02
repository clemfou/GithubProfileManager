"""Handle API requests."""

import json

from typing import Optional
import requests

from urllib3.exceptions import HTTPError

from github_profile_manager import global_variables as globs
from github_profile_manager.utils.config import APIConfig


class GithubAPI:
    """Handle the requests to the github API."""

    def __init__(self, config: APIConfig) -> None:
        """Initialize the GithubAPI class."""
        self.base_url = config.base_url
        self.token = config.token
        self.session = requests.Session()
        self.set_headers()

    def set_headers(self, other_headers=None) -> None:
        """Handle HTTP GET requests."""
        headers = {
            "Authorization": f"Bearer {self.token.get_secret_value()}",
        }
        if other_headers:
            headers.update(other_headers)

        return self.session.headers.update(headers)

    def _handle_response(self, response: requests.Response) -> Optional[list]:
        """Handle HTTP responses."""
        if response.status_code >= 200 and response.status_code <= 299:
            globs.LOGGER.debug("%s: Operation successful", response.status_code)

        else:
            raise HTTPError(f"{response.status_code}: {response.reason}")

        if response.text:
            try:
                return response.json()

            except ValueError:
                globs.LOGGER.warning("Invalid JSON response")

        return None

    def get(self, endpoint: str) -> Optional[list]:
        """Handle HTTP GET requests."""
        url = f"{self.base_url}/{endpoint}"

        try:
            response = self.session.get(url)

        except requests.exceptions.RequestException as e:
            globs.LOGGER.error(e)

        return self._handle_response(response)

    def post(self, endpoint: str, data=None) -> Optional[list]:
        """Handle HTTP POST requests."""
        url = f"{self.base_url}/{endpoint}"
        data = json.dumps(data)

        try:
            response = self.session.post(url, data)

        except requests.exceptions.RequestException as e:
            globs.LOGGER.error(e)

        return self._handle_response(response)

    def delete(self, endpoint: str) -> Optional[list]:
        """Handle HTTP DELETE requests."""
        url = f"{self.base_url}/{endpoint}"

        try:
            response = self.session.delete(url)

        except requests.exceptions.RequestException as e:
            globs.LOGGER.error(e)

        return self._handle_response(response)

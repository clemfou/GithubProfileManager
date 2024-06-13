"""Global variables."""

from __future__ import annotations

from github_profile_manager.api import GithubAPI
from github_profile_manager.utils.config import Config  # noqa: TCH001

GITHUB_API: GithubAPI | None = None
CONFIG: Config | None = None
LOGGER = None

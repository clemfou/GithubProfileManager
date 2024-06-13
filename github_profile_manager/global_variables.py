"""Global variables."""
# ruff: noqa: TCH001

from __future__ import annotations

from github_profile_manager.api import GithubAPI
from github_profile_manager.utils.config import Config

GITHUB_API: GithubAPI | None = None
CONFIG: Config | None = None
LOGGER = None

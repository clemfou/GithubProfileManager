"""Main package entrypoint."""

import logging
import logging.config
import sys
from pathlib import Path

from github_profile_manager import global_variables as globs
from github_profile_manager.api import GithubAPI
from github_profile_manager.utils.config import Config
from github_profile_manager.utils.logging import setup_logger
from github_profile_manager.utils.parser import parse_args


def load_configuration(configuration_file: Path) -> Config:
    """Load the configuration file."""
    try:
        configuration = Config.parse_file(configuration_file)

    except Exception:
        logging.exception("Cannot load the configuration file")
        sys.exit(1)

    return configuration


def main() -> None:
    """Entry point."""
    args = parse_args(sys.argv[1:])
    globs.CONFIG = load_configuration(args.config)

    globs.LOGGER = setup_logger()
    globs.GITHUB_API = GithubAPI(globs.CONFIG.api_config)

    if "func" in args:
        args_dict = vars(args).copy()

        del args_dict["config"]
        del args_dict["func"]

        try:
            args.func(**args_dict)

        except Exception as err:  # noqa: BLE001
            globs.LOGGER.error(err)

"""Main package entrypoint."""

import logging
import logging.config
import sys
from pathlib import Path

from github_profile_manager import global_variables as globs
from github_profile_manager.account import GithubAccount
from github_profile_manager.utils.config import Config
from github_profile_manager.utils.parser import parse_args


def load_configuration(configuration_file: Path) -> Config:
    """Load the configuration file."""
    try:
        configuration = Config.parse_file(configuration_file)

    except Exception:
        logging.exception()
        sys.exit(1)

    return configuration


def setup_logger() -> logging.Logger:
    """Set up the logging module."""
    logger_config = globs.CONFIG.logging_config.dict(by_alias=True)
    logging.config.dictConfig(logger_config)

    return logging.getLogger(__name__)


def main() -> None:
    """Entry point."""
    args = parse_args(sys.argv[1:])
    globs.CONFIG = load_configuration(args.config)

    globs.LOGGER = setup_logger()

    if "func" in args:
        github_account = GithubAccount()
        args_dict = vars(args).copy()

        del args_dict["config"]
        del args_dict["func"]

        try:
            args.func(github_account, **args_dict)

        except Exception as err:  # noqa: BLE001
            globs.LOGGER.error(err)

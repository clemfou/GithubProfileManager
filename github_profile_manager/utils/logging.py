"""Handle the logging module."""

from __future__ import annotations

import json
import logging
import logging.config

from github_profile_manager import global_variables as globs


class CustomFormatter(logging.Formatter):
    """Dump logging messages in json."""

    def __init__(
        self,
        fmt: str | None = None,  # noqa: ARG002
        datefmt: str | None = None,  # noqa: ARG002
        style: str = "%",  # noqa: ARG002
    ) -> None:
        """Init the CustomFormatter."""
        self.default_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        self.default_datefmt = "%Y-%m-%d %H:%M:%S"
        self.default_formatter = logging.Formatter(self.default_fmt, self.default_datefmt)

    def format(self, record: logging.LogRecord) -> str:
        """Format the logging message."""
        if hasattr(record, "extra"):
            return json.dumps(record.extra, indent=2)

        return self.default_formatter.format(record)


def setup_logger() -> logging.Logger:
    """Set up the logging module."""
    logger_config = globs.CONFIG.logging_config.dict(by_alias=True)
    logging.config.dictConfig(logger_config)

    return logging.getLogger(__name__)

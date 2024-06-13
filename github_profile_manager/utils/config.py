# ruff: noqa: FA100
"""Handle configuration files."""

from typing import Dict, List, Optional

from pydantic import AnyHttpUrl, BaseModel, Field, SecretStr


class FormatterConfig(BaseModel):
    """Formatter configuration for the logging module."""

    format: Optional[str] = None
    class_: str = Field(None, alias="class")


class HandlerConfig(BaseModel):
    """Handler configuration for the logging module."""

    # class is a reserved keyword
    class_: str = Field(..., alias="class")
    level: str
    formatter: str
    stream: str


class LoggerConfig(BaseModel):
    """Logger configuration for the logging module."""

    level: str
    handlers: List[str]
    propagate: bool


class RootConfig(BaseModel):
    """Root logger configuration for the logging module."""

    level: str
    handlers: List[str]


class LoggingConfig(BaseModel):
    """Logging module configuration."""

    version: int
    disable_existing_loggers: bool
    formatters: Dict[str, FormatterConfig]
    handlers: Dict[str, HandlerConfig]
    loggers: Dict[str, LoggerConfig]
    root: RootConfig


class APIConfig(BaseModel):
    """Github API configuration settings."""

    base_url: AnyHttpUrl
    token: SecretStr


class Config(BaseModel):
    """Program settings."""

    api_config: APIConfig
    logging_config: LoggingConfig

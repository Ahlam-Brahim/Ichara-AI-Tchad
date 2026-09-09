"""
Logging utilities for Ichara AI Tchad.

Provides a centralized logging configuration so that all project
modules can use consistent log messages.
"""

from __future__ import annotations

import logging
import sys
from typing import Optional


DEFAULT_LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | "
    "%(name)s | %(message)s"
)


def get_logger(
    name: str,
    level: int = logging.INFO,
) -> logging.Logger:
    """
    Create or retrieve a project logger.

    Args:
        name: Logger name.
        level: Logging level.

    Returns:
        Configured logger instance.
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)

        formatter = logging.Formatter(DEFAULT_LOG_FORMAT)
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    logger.setLevel(level)
    logger.propagate = False

    return logger


def set_log_level(
    logger: logging.Logger,
    level: int,
) -> None:
    """
    Change the logging level of an existing logger.

    Args:
        logger: Logger to configure.
        level: New logging level.
    """
    logger.setLevel(level)


def configure_root_logger(
    level: int = logging.INFO,
    log_format: Optional[str] = None,
) -> None:
    """
    Configure the root logger for the application.

    Args:
        level: Default logging level.
        log_format: Optional custom logging format.
    """
    logging.basicConfig(
        level=level,
        format=log_format or DEFAULT_LOG_FORMAT,
        stream=sys.stdout,
        force=True,
    )

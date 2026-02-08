"""Logging setup helpers."""

import logging

from app.core.config import settings


def configure_logging() -> None:
    """Configure the root logger."""
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

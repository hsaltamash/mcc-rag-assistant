"""Main application entrypoint."""

from app.core.config import settings
from app.core.logging import configure_logging


def run() -> None:
    """Initialize logging and print a startup message."""
    configure_logging()
    print(f"MCC RAG Assistant starting in {settings.environment} mode")


if __name__ == "__main__":
    run()

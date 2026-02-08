"""Application configuration settings."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the service."""

    environment: str = "development"
    log_level: str = "INFO"
    vector_store_path: str = "data/chroma"


settings = Settings()

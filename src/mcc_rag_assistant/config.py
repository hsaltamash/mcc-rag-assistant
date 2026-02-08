"""Configuration models for the assistant."""

from pydantic import BaseModel, Field


class AssistantConfig(BaseModel):
    """Runtime configuration for the assistant."""

    index_path: str = Field(default="data/index", description="Path to the vector index.")
    top_k: int = Field(default=5, ge=1, le=50, description="Number of chunks to retrieve.")
    temperature: float = Field(default=0.2, ge=0.0, le=1.0, description="Sampling temperature.")
    model_name: str = Field(default="gpt-4o-mini", description="Model identifier.")

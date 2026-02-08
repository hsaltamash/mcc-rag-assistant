"""CLI entrypoint for the assistant scaffold."""

from __future__ import annotations

import json
from typing import Optional

import typer
from rich.console import Console

from mcc_rag_assistant.config import AssistantConfig

app = typer.Typer(add_completion=False)
console = Console()


@app.command()
def show_config(
    index_path: Optional[str] = typer.Option(None, help="Path to the vector index."),
    top_k: Optional[int] = typer.Option(None, min=1, max=50, help="Number of chunks to retrieve."),
    temperature: Optional[float] = typer.Option(None, min=0.0, max=1.0, help="Sampling temperature."),
    model_name: Optional[str] = typer.Option(None, help="Model identifier."),
) -> None:
    """Print the resolved configuration for the assistant."""

    config = AssistantConfig(
        index_path=index_path or AssistantConfig().index_path,
        top_k=top_k or AssistantConfig().top_k,
        temperature=temperature or AssistantConfig().temperature,
        model_name=model_name or AssistantConfig().model_name,
    )
    console.print_json(json.dumps(config.model_dump()))


if __name__ == "__main__":
    app()

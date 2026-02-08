"""Admin documentation routes."""

from pathlib import Path


def list_seed_docs(seed_dir: Path) -> list[str]:
    """List available seed documents."""
    return [path.name for path in sorted(seed_dir.glob("*.md"))]

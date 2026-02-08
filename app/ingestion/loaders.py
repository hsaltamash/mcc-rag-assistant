"""Document loading utilities."""

from pathlib import Path
from typing import List


def load_markdown(path: Path) -> str:
    """Load a markdown file from disk."""
    return path.read_text(encoding="utf-8")


def load_markdown_dir(directory: Path) -> List[str]:
    """Load all markdown files in a directory."""
    return [load_markdown(path) for path in sorted(directory.glob("*.md"))]

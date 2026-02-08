from pathlib import Path
from pypdf import PdfReader


def load_text_from_file(path: Path) -> str:
    if path.suffix.lower() in [".md", ".txt"]:
        return path.read_text(encoding="utf-8", errors="ignore")

    if path.suffix.lower() == ".pdf":
        reader = PdfReader(str(path))
        parts = []
        for page in reader.pages:
            parts.append(page.extract_text() or "")
        return "\n".join(parts)

    raise ValueError(f"Unsupported file type: {path.suffix}")

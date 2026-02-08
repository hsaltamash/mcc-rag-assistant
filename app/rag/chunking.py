def chunk_text(text: str, max_chars: int = 1200, overlap: int = 200) -> list[str]:
    text = " ".join(text.split())
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i : i + max_chars])
        i += max_chars - overlap
    return chunks

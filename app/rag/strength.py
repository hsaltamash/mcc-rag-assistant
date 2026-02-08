"""RAG strength scoring placeholder."""


def score_strength(answer: str) -> float:
    """Score how confident the system is in the answer."""
    return min(1.0, max(0.0, len(answer) / 100.0))

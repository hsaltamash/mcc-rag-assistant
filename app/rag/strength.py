from __future__ import annotations

import re
from typing import List, Tuple


def _has_citations(answer: str) -> bool:
    return bool(re.search(r"\[\d+\]", answer))


def compute_strength(
    distances: List[float],
    answer: str,
    min_high: float = 0.25,
    min_medium: float = 0.40,
) -> Tuple[str, str]:
    """
    Chroma distances: smaller is better (closer vectors).
    Heuristic mapping:
      - High: close retrieval + citations
      - Medium: decent retrieval or citations missing
      - Low: weak retrieval OR no retrieval
    """
    if not distances:
        return ("Low", "No relevant context retrieved.")

    best = distances[0]
    cites = _has_citations(answer)

    if best <= min_high and cites:
        return ("High", f"Strong match to documents (best distance={best:.3f}) with citations.")

    if best <= min_medium:
        if cites:
            return ("Medium", f"Moderate match (best distance={best:.3f}); answer includes citations.")
        return ("Medium", f"Moderate match (best distance={best:.3f}); citations missing or incomplete.")

    if cites:
        return ("Low", f"Weak match (best distance={best:.3f}); citations may not be reliable.")
    return ("Low", f"Weak match to documents (best distance={best:.3f}).")

from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class Citation:
    url: str
    content: str


class CitationManager:
    """Store citations for a research task."""

    def __init__(self) -> None:
        self._citations: List[Citation] = []

    def add(self, url: str, content: str) -> None:
        self._citations.append(Citation(url=url, content=content))

    def list(self) -> List[Citation]:
        return list(self._citations)

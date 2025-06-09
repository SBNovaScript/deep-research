from __future__ import annotations
from dataclasses import dataclass
from typing import List
import logging


@dataclass
class Citation:
    url: str
    content: str


class CitationManager:
    """Store citations for a research task."""

    def __init__(self) -> None:
        self._citations: List[Citation] = []
        self.logger = logging.getLogger(__name__)

    def add(self, url: str, content: str) -> None:
        self._citations.append(Citation(url=url, content=content))
        self.logger.debug("Citation added for %s", url)

    def list(self) -> List[Citation]:
        return list(self._citations)

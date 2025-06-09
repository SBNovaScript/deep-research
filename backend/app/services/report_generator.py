from __future__ import annotations

from typing import List
import logging

from .citation_manager import CitationManager


class ReportGenerator:
    """Compile summaries and citations into a report."""

    def __init__(self, citation_manager: CitationManager) -> None:
        self.citations = citation_manager
        self.logger = logging.getLogger(__name__)

    def generate(self, summaries: List[str]) -> str:
        self.logger.info("Generating final report")
        report_sections = [s for s in summaries if s]
        return "\n\n".join(report_sections)

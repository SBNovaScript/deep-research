from __future__ import annotations

import logging
from .ai_connectors import AIConnector
from ..prompts import SUMMARY_TEMPLATE


class Summarizer:
    """Use an AIConnector to summarize text."""

    def __init__(self, connector: AIConnector):
        self.connector = connector
        self.logger = logging.getLogger(__name__)

    async def summarize(self, text: str) -> str:
        prompt = SUMMARY_TEMPLATE.format(text=text[:500])
        self.logger.debug("Summarizing text of length %d", len(text))
        return await self.connector.complete(prompt)

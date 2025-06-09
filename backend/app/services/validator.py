from __future__ import annotations

import logging
from .ai_connectors import AIConnector
from ..prompts import FACT_CHECK_TEMPLATE, BIAS_CHECK_TEMPLATE


class Validator:
    """Run fact and bias checks using an AIConnector."""

    def __init__(self, connector: AIConnector) -> None:
        self.connector = connector
        self.logger = logging.getLogger(__name__)

    async def fact_check(self, text: str) -> str:
        prompt = FACT_CHECK_TEMPLATE.format(text=text[:500])
        self.logger.debug("Running fact check")
        return await self.connector.complete(prompt)

    async def bias_check(self, text: str) -> str:
        prompt = BIAS_CHECK_TEMPLATE.format(text=text[:500])
        self.logger.debug("Running bias check")
        return await self.connector.complete(prompt)

from __future__ import annotations

import asyncio
import os
import logging
from typing import List, Set

from googleapiclient.discovery import build


class GoogleSearch:
    """Use Google Custom Search API to fetch result URLs asynchronously."""

    def __init__(self, api_key: str | None = None, cse_id: str | None = None, per_query: int = 5) -> None:
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self.cse_id = cse_id or os.getenv("GOOGLE_CSE_ID")
        if not self.api_key or not self.cse_id:
            raise ValueError("Google API key and CSE ID must be provided")
        self.per_query = per_query
        self.service = build("customsearch", "v1", developerKey=self.api_key, cache_discovery=False)
        self.logger = logging.getLogger(__name__)

    def _sync_search(self, query: str) -> List[str]:
        self.logger.debug("Searching Google for %s", query)
        result = (
            self.service.cse()
            .list(q=query, cx=self.cse_id, num=self.per_query)
            .execute()
        )
        links = [item["link"] for item in result.get("items", [])]
        self.logger.debug("Found %d links for %s", len(links), query)
        return links

    async def _search(self, query: str) -> List[str]:
        return await asyncio.to_thread(self._sync_search, query)

    async def search_all(self, queries: List[str]) -> List[str]:
        results: List[str] = []
        seen: Set[str] = set()
        for query in queries:
            for url in await self._search(query):
                if url not in seen:
                    seen.add(url)
                    results.append(url)
        self.logger.info("Google search produced %d unique URLs", len(results))
        return results

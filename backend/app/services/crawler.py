from __future__ import annotations
import logging
import aiohttp
from typing import List, Tuple

from ..utils.files import save_text


async def fetch(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url) as resp:
        resp.raise_for_status()
        return await resp.text()


class WebCrawler:
    """Simple asynchronous web crawler."""

    async def crawl(self, task_id: str, urls: List[str]) -> List[Tuple[str, str]]:
        logger = logging.getLogger(__name__)
        results: List[Tuple[str, str]] = []
        async with aiohttp.ClientSession() as session:
            for idx, url in enumerate(urls):
                try:
                    logger.debug("Fetching %s", url)
                    text = await fetch(session, url)
                    save_text(task_id, f"{idx}.html", text)
                    results.append((url, text))
                except Exception as exc:
                    logger.warning("Failed to fetch %s: %s", url, exc)
                    # Skip pages that fail to load
                    continue
        return results

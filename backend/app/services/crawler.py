from __future__ import annotations
import logging
from typing import List, Tuple

from ..utils.files import save_text

from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError


async def fetch_with_browser(url: str, timeout: int = 30) -> str:
    """Fetch a page using a headless browser and wait for full load.

    Parameters
    ----------
    url: str
        Target URL to visit.
    timeout: int
        Timeout in seconds to wait for the page to load.
    """
    timeout_ms = timeout * 1000
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/114.0 Safari/537.36"
            )
        )
        page = await context.new_page()
        try:
            await page.goto(url, wait_until="networkidle", timeout=timeout_ms)
            content = await page.content()
        finally:
            await page.close()
            await browser.close()
        return content


class WebCrawler:
    """Simple asynchronous web crawler."""

    async def crawl(self, task_id: str, urls: List[str]) -> List[Tuple[str, str]]:
        logger = logging.getLogger(__name__)
        results: List[Tuple[str, str]] = []
        for idx, url in enumerate(urls):
            try:
                logger.debug("Fetching %s", url)
                text = await fetch_with_browser(url, timeout=30)
                save_text(task_id, f"{idx}.html", text)
                results.append((url, text))
            except PlaywrightTimeoutError as exc:
                logger.warning("Timeout fetching %s: %s", url, exc)
                continue
            except Exception as exc:
                logger.warning("Failed to fetch %s: %s", url, exc)
                # Skip pages that fail to load
                continue
        return results

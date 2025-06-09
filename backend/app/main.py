from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .utils.logging import setup_logging

from .api import router as api_router
from .services import research_runner


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await research_runner.shutdown()


setup_logging()
app = FastAPI(lifespan=lifespan)
# Allow CORS requests only from localhost, regardless of scheme or port.
# Using a regex lets us match http://localhost, https://127.0.0.1, etc.
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^https?://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)

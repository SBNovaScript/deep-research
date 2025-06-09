from fastapi import FastAPI
from contextlib import asynccontextmanager

from .api import router as api_router
from .services import research_runner


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await research_runner.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

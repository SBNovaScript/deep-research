from fastapi import APIRouter
from . import health, research

router = APIRouter()
router.include_router(health.router)
router.include_router(research.router)

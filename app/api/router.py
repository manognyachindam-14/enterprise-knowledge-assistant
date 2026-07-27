from fastapi import APIRouter

from app.api.documents import router as document_router
from app.api.health import router as health_router


api_router = APIRouter()

api_router.include_router(
    health_router,
    tags=["Health"],
)

api_router.include_router(
    document_router,
    tags=["Documents"],
)
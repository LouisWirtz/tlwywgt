"""Health check endpoint."""
from fastapi import APIRouter

from app.models.health_models import HealthResponse

router = APIRouter()


@router.get('/health', response_model=HealthResponse)
async def health() -> HealthResponse:
    """Get health response."""
    return HealthResponse(health=True)

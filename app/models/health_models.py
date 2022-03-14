"""Model for health status."""
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Describes the response for health."""

    health: bool

from pydantic import BaseModel


class HealthResponse(BaseModel):
    health: bool
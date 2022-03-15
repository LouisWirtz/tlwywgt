"""Common models."""
from pydantic import BaseModel


class SelfRef(BaseModel):
    """Selflink representation."""

    self: str  # noqa: WPS117

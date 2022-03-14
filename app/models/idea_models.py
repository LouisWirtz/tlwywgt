"""Model for ideas."""
import datetime

from pydantic import BaseModel, Field

max_title_length = 50


class IdeaResponse(BaseModel):
    """Describes the response for one idea."""

    identity: int
    title: str = Field(..., max_length=max_title_length)
    date: datetime.datetime
    description: str
    # TODO: SexyFrosch.png

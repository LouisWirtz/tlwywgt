"""Model for ideas."""
import datetime

from pydantic import Field

from app.models import commons

max_title_length = 50


class IdeaResponse(commons.SelfRef):
    """Describes the response for one idea."""

    title: str = Field(..., max_length=max_title_length)
    date: datetime.datetime
    description: str

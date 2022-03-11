import datetime

from pydantic import BaseModel, Field


class IdeaResponse(BaseModel):
    id: int
    title: str = Field(..., max_length=50)
    date: datetime.datetime
    description: str
    # TODO: SexyFrosch.png

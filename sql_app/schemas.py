"""Schemas for common attributes while creating or reading data."""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class IdeaBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: datetime
    # TODO: image: file --> how do I do this?

    class Config:
        """Provides configurations to pydantic.
        The pydantic model will read data even if it is not a dict, but an ORM model."""
        orm_mode = True


class IdeaCreate(IdeaBase):
    pass


class Idea(IdeaBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
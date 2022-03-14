"""Idea related endpoint."""
import datetime

from fastapi import APIRouter

from app.models.idea_models import IdeaResponse

router = APIRouter()


@router.get('/idea/{identity}', response_model=IdeaResponse)
async def idea(identity: int) -> IdeaResponse:
    """Get specific idea."""
    return IdeaResponse(
        identity=0, title='TestIdee', date=datetime.datetime.now(), description='Meine Tolle idee Subscribe',
    )

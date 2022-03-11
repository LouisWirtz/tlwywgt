import datetime

from fastapi import APIRouter

from app.models.idea_models import IdeaResponse

router = APIRouter()


@router.get('/idea/{id}', response_model=IdeaResponse)
async def idea(id: int) -> IdeaResponse:
    return IdeaResponse(id=0, title='TestIdee', date=datetime.datetime.now(), description='Meine Tolle idee Subscribe')

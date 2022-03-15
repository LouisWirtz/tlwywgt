"""Idea related endpoint."""
import datetime
from typing import List

from fastapi import APIRouter, Path, Request

from app.models import commons
from app.models.idea_models import IdeaResponse

path_prefix = '/ideas'
router = APIRouter(prefix=path_prefix)


@router.get('/', response_model=List[commons.SelfRef])
async def ideas() -> List[commons.SelfRef]:
    """Get available ideas."""
    self_link_template = '{path_prefix}/{id}'

    return [
        commons.SelfRef(self=self_link_template.format(path_prefix=path_prefix, id=1)),
        commons.SelfRef(self=self_link_template.format(path_prefix=path_prefix, id=2)),
        commons.SelfRef(self=self_link_template.format(path_prefix=path_prefix, id=3)),
    ]


@router.get('/{id}', response_model=IdeaResponse)
async def idea(
    request: Request,
    idea_id: int = Path(..., alias='id'),
) -> IdeaResponse:
    """Get specific idea."""
    return IdeaResponse(
        title='TestIdee',
        date=datetime.datetime.now(),
        description='Meine Tolle idee Subscribe',
        self=request.url.path,
    )

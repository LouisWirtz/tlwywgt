"""Image related endpoint."""
import datetime
from typing import List

from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

from app.models import commons

file_path = "./ressources/img/sexy_frog.jpg"
router = APIRouter()


@router.get("/images", response_class=FileResponse)
async def main():
    """Get default image."""
    return file_path


from fastapi import APIRouter
from config import settings

router = APIRouter()

@router.get("/settings", tags=["Settings"])
async def read_settings():

    return {"DB_URL": settings.DB_URL}

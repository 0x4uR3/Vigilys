from fastapi import APIRouter
from backend.config import conf

router = APIRouter()

@router.get("/settings", tags=["Settings"])
async def read_settings():

    return {"DB_URL": conf.DB_URL}

from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
from typing import List, Optional
from sqlalchemy.orm import Session

from backend.schemas import user_schema
from backend.database import get_db
from backend.repositories import user_repo

router = APIRouter()

@router.get("/users", tags=["Users"], response_model=List[user_schema.User])
async def get_all_users(username: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Get all the Users stored in database
    """
    if username:
        users =[]
        db_user = user_repo.fetch_by_username(db, username)
        users.append(db_user)
        return users
    else:
        return user_repo.UserRepo.fetch_all(db)
    

@router.get('/user/{username}', tags=["User"],response_model=user_schema.User)
async def get_user(username: int, db: Session = Depends(get_db)):
    """
    Get the Device with the given no_device provided by User stored in database
    """
    db_user = user_repo.UserRepo.fetch_by_username(db, username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found with the given no_device")
    return db_user
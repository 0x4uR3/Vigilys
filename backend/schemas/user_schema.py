from typing import List, Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str
    level: int
    status: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    class Config:
        from_attributes = True

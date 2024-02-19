from sqlalchemy.orm import Session

from backend.models import user_model
from backend.schemas import user_schema

class UserRepo:
    async def create(db: Session, user: user_schema.UserCreate):
        db_user = user_model.Users(username=user.username,
                                    password=user.password,
                                    level=user.level,
                                    status=user.status)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def fetch_by_username(db: Session, username):
        return db.query(user_model.Users).filter(user_model.Users.username == username).first()

    def fetch_by_level(db: Session, level):
        return db.query(user_model.Users).filter(user_model.Users.level == level).first()
    
    def fetch_by_status(db: Session, status):
        return db.query(user_model.Users).filter(user_model.Users.status == status).first()

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(user_model.Devices).offset(skip).limit(limit).all()

    async def delete(db: Session, username):
        db_user= db.query(user_model.Users).filter_by(username=username).first()
        db.delete(db_user)
        db.commit()
        
    async def update(db: Session, user_data):
        updated_user = db.merge(user_data)
        db.commit()
        return updated_user
 
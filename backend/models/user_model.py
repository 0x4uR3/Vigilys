from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.database import Base
    
class Users(Base):
    __tablename__ = "users"
    username = Column(String(30), primary_key=True, index=True, nullable=False)
    password = Column(String(50), nullable=False)
    level = Column(Integer, nullable=False, index=True, default=1)
    status = Column(Integer, nullable=False, index=True, default=1)
    def __repr__(self):
        return 'User(username=%s)' % (self.username)

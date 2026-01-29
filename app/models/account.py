from sqlalchemy import Column, Integer, Float, ForeignKey
from app.database.base import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    balance = Column(Float, default=0)
    user_id = Column(Integer, ForeignKey("users.id"))

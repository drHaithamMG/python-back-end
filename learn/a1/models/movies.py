from typing import Optional
from pydantic import BaseModel
# from pydantic.types import UUID4
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, Text,Float,DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relation

from db.db import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name: Column(String)
    rate: Column(Float)
    production_date: Column(DateTime ,default=datetime.now)
    pic: Column(Text)
    


class Movies(BaseModel):
    id: int
    name: str
    rate: float
    production_date: datetime
    pic: str
    details_id: int

class MovieOut(BaseModel):
    name:str
    pic:str
    rate:float

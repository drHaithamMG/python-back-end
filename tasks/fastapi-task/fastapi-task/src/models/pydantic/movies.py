from pydantic import BaseModel, HttpUrl
from pydantic.types import UUID4
from datetime import datetime, date


class Movie(BaseModel):

    uuid: UUID4
    title: str
    production_date: date
    rate: float
    picture: HttpUrl
    create_at: date = datetime
    update_at: date = datetime


class MovieOut(BaseModel):
    uuid: UUID4
    title: str
    production_date: datetime
    rate: float
    picture: HttpUrl


class CustomeMessages(BaseModel):
    message: str

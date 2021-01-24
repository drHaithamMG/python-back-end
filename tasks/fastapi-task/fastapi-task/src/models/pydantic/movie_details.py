from pydantic import BaseModel
from pydantic.types import UUID4
from datetime import datetime, date


class MovieDetails(BaseModel):
    uuid: UUID4
    catagories: str
    production_company: str
    price: float
    overview: str
    create_at: date = datetime.now()
    update_at: date = datetime.now()


class MovieDetailsOut(BaseModel):
    uuid: UUID4
    catagories: str
    production_company: str
    price: float
    overview: str


from uuid import uuid4
from sqlalchemy import Column, String, Date, Float, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float
from src.models.movies import MoviesSQL

from controller import Base


class MoviesDetailsSQL(Base):
    __tablename__ = "Movie Details"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid4)
    overview = Column(Text)
    production_company = Column(String)
    price = Column(Float)
    catagories = Column(String)
    movie_relationship=relationship("MoviesSQL",back_populates="movie_details_relationship")
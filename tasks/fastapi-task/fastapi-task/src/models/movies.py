from uuid import uuid4
from sqlalchemy import Column, String, Date, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float
from src.models.movie_details import MoviesDetailsSQL
from controller import Base


class MoviesSQL(Base):
    __tablename__ = "Movies"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid4)
    title = Column(String)
    production_date = Column(Date)
    rate = Column(Float)
    picture = Column(String)
    movie_details = Column(UUID(as_uuid=True), ForeignKey(MoviesDetailsSQL.id))
    movie_details_relationship = relationship(
        "MovieDetailsSQL", back_populates="movie_relationship")

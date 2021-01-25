from uuid import uuid4
from sqlalchemy import Column, String, Date, Float
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float
from src.models.base import BaseORM


class MoviesSQL(BaseORM):
    __tablename__ = "Movies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(200))
    production_date = Column(Date)
    rate = Column(Float)
    picture = Column(String)
    # movie_details_id = Column(
    #     'movie_details_id', UUID(), ForeignKey('movie_details.id'))
    # movie_details_relationship = relationship(
    #     "MovieDetailsSQL", back_populates="movie_relationship")
    class Config:
        orm_mode = True
    meta = Column(postgresql.JSONB, index=False, nullable=True)

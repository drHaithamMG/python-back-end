# from uuid import uuid4
# from sqlalchemy import Column, String, Date, Float, Text
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql.sqltypes import Float
# from src.models.base import BaseORM
# from src.models import Base

# class MoviesDetailsSQL(Base,BaseORM):
#     __tablename__ = "movie_details"

#     id = Column(UUID(as_uuid=True), primary_key=True,
#                 index=True, default=uuid4)
#     overview = Column(Text)
#     production_company = Column(String(200))
#     price = Column(Float)
#     catagories = Column(String(100))
#     movie_relationship = relationship(
#         "MoviesSQL", back_populates="movie_details_relationship")
#     class Config:
#          orm_mode = True

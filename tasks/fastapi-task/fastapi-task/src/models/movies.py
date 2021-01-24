from uuid import uuid4
from sqlalchemy import Column, String,Date,Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Float

from settings.db import Base


class Post(Base):
    __tablename__ = "Movies"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    title = Column(String)
    production_date= Column(Date)
    rate = Column(Float)
    picture = Column(String)

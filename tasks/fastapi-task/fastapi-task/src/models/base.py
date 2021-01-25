from src.models import sessionmaker, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base


class BaseORM(DeclarativeBase):
    __abstract__ = True

    def __init__(self):
        self.session = sessionmaker

    def get_all(self):
        return self.session.query(self.__class__).all()

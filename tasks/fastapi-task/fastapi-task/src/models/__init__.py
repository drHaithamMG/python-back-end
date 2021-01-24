from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "postgresql://haitham:351996@localhost/okay"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_by_id(db: Session, id: uuid4, obj: object):
    return db.query(obj).filter(id == obj.id).first()


def get_all(db: Session, obj: object):
    return db.query(obj).all()


def add_element(db: Session, obj: object):
    pass

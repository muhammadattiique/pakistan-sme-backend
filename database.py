from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./business.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False,
)


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""
    pass


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def get_db():
    """
    FastAPI database dependency.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
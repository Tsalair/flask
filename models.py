import os
import atexit
import datetime

from sqlalchemy import DateTime, String, create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "ads_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)

atexit.register(engine.dispose)


class Base(DeclarativeBase):
    pass

class Ad(Base):
    __tablename__= 'ads'

    id: Mapped[int] = mapped_column(primary_key=True)
    header: Mapped[str] = mapped_column(
        String(100), unique=False, index=True, nullable=False)
    text: Mapped[str] = mapped_column(
        String(500), nullable=False)
    registration_time: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now())
    owner: Mapped[str] = mapped_column(
        String(50), unique=False, index=True, nullable=False)
    

    @property
    def dict(self):
        return {
            "id": self.id,
            "header": self.header,
            "text": self.text,
            "registration_time": self.registration_time.isoformat(),
            "owner": self.owner
        }
    

Base.metadata.create_all(bind=engine)
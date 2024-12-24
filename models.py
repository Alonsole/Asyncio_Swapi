import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

dotenv_file = '.env'
load_dotenv(dotenv_file)

POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")
POSTGRES_USER = os.getenv("POSTGRES_USER", "swapi")
POSTGRES_DB = os.getenv("POSTGRES_DB", "swapi")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")


PG_DSN = (
    f"postgresql+asyncpg://"
    f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_async_engine(PG_DSN)
Session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):
    pass


class SwapiPeople(Base):
    __tablename__ = "swapi_people"
    id = Column(Integer, primary_key=True)
    birth_year = Column(String())
    eye_color = Column(String())
    films = Column(String(), nullable=True)  # - строка с названиями фильмов через запятую
    gender = Column(String())
    hair_color = Column(String())
    height = Column(String())
    homeworld = Column(String())
    mass = Column(String())
    name = Column(String())
    skin_color = Column(String())
    species = Column(String())   # - строка с названиями типов через запятую
    starships = Column(String())   # - строка с названиями кораблей через запятую
    vehicles = Column(String())   # - строка с названиями транспорта через запятую


async def init_orm():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_orm():
    await engine.dispose()
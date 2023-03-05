from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import ASYNC_DB_URL, DB_URL


engine = create_engine(DB_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(autocommit=False, bind=engine, autoflush=True) # создание подключения к бд
session = Session()

def get_session():
    return session

# async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
# async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

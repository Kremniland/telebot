from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Column, Integer, String, BigInteger, UnicodeText, Text, ForeignKey
)

from config import ASYNC_DB_URL, DB_URL


engine = create_engine(DB_URL, echo=True)
Base = declarative_base()
session = sessionmaker(autocommit=True, bind=engine, autoflush=True) # создание подключения к бд


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True)
    user_tg_id = Column(String, nullable=False, unique=True) # телеграмм ид пользователя
    points = Column(BigInteger,default=0) # колличество очков пользователя


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True)
    name = Column(String(100), nullable=False)


class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True)
    emoji_text = Column(UnicodeText, nullable=False)
    name_text = Column(Text, nullable=False)
    category = Column(Integer, ForeignKey('category.id'), nullable=False)

Base.metadata.create_all(engine, checkfirst=True)

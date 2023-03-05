from sqlalchemy import (
    Column, Integer, String, BigInteger, UnicodeText, Text, ForeignKey
)

from Project_3.db import Base, engine


# def create_tables():
#     '''создает все таблицы в базе'''
#     Base.metadata.create_all(engine, checkfirst=True) # создаст все таблицы созданные на основе Base


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True)
    user_tg_id = Column(String, nullable=False, unique=True) # телеграмм ид пользователя
    points = Column(BigInteger,default=0) # колличество очков пользователя


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True)
    name = Column(String(100), nullable=False)


class Film(Base):
    __tablename__ = 'film'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True)
    emoji_text = Column(UnicodeText, nullable=False)
    name_text = Column(Text, nullable=False)
    category = Column(Integer, ForeignKey('category.id'), nullable=False)


# без этого импорта не будет работать!!!!!!!!!!!!!
from database.models import Category, Film # без этого импорта не будет работать!!!!!!!!!!!!!
from Project_3.db import Base, engine


def create_tables():
    '''создает все таблицы в базе'''
    Base.metadata.create_all(engine, checkfirst=True) # создаст все таблицы созданные на основе Base
                                                    # checkfirst=True - проверяет есть ли таблицы

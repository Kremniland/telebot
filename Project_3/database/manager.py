from Project_3.database.models import Category, User, Film
from Project_3.db import get_session


class CategoryManager():
    def __init__(self):
        self.model = Category
        self.session = get_session()

    def insert_category(self, data):
        '''добавление в базу новой категории'''
        inserts = []

        for category in data: # data список категорий из csv файла
            inserts.append(
                Category(
                    name=category[0]
                )
            )
        self.session.add_all(inserts)
        self.session.commit()
        # ===== или вот так:
        # for c in data:
        #     category = Category(name=c[0])
        #     self.session.add(category)
        #     self.session.commit()

    def get_all_categories(self):
        '''получение всех категорий из базы'''
        results = self.session.query(self.model).all()
        return results


class FilmManager():
    def __init__(self):
        self.session = get_session()
        self.model = Film

    def insert_film(self, data):
        '''добавляем фильмы в базу'''
        inserts = []
        for film in data:
            inserts.append(
                Film(
                    emoji_text=film[0],
                    name_text=film[1],
                    category=film[2]
                )
            )
        self.session.add_all(inserts)
        self.session.commit()

    def get_films(self):
        results = self.session.query(self.model).all()
        return results




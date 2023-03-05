from Project_3.database.models import Category, User, Film
from Project_3.db import get_session


class CategoryManager():
    def __init__(self):
        self.model = Category
        self.session = get_session()

    def insert_category(self, data):
        '''добавление в базу новой категории'''
        inserts = []

        for c in data: # data список категорий из csv файла
            inserts.append(
                Category(
                    name=c[0]
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



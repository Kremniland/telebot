from sqlalchemy import not_
from sqlalchemy.sql import func

from Project_3.database.models import Category, Film, UserGuessedFilm
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

    def get_random_film(self, film_ids, category_id=None):
        if category_id:
            # отдаст все фильмы категории которой мы запросили кроме id из списка film_ids
            q = self.session.query(self.model).filter(
                not_(Film.id.in_(film_ids)),
                # !!!!что бы написать равно пишем модель.поле == атрибут
                Film.category == category_id
            ).order_by(func.random()).first() # вернет рандомно первый из списка
            return q
        else:
            # отдаст все фильмы которых нет в списке переданных film_ids
            q = self.session.query(self.model).filter(
                not_(Film.id.in_(film_ids)),
            ).order_by(func.random()).first() # вернет рандомно первый из списка
            return q


class GuessedFilmManager():
    def __init__(self):
        self.session = get_session()
        self.models = UserGuessedFilm

    def insert_guessed_film(self, tg_user_id, film_id):
        '''добавление пользователя и фильм в модель UserGuessedFilm'''
        insert = UserGuessedFilm(
            tg_user_id=tg_user_id,
            film = film_id
        )
        self.session.add(insert)
        self.session.commit()

    def get_guessed_film(self, tg_user_id):
        '''получаем все id из модели UserGuessedFilm, где tg_user_id=tg_user_id,
        т е список фильмов которые пользователь уже угадал'''
        results = self.session.query(UserGuessedFilm.id).filter(
            # !!!что бы написать равно пишем модель.поле == атрибут
            UserGuessedFilm.tg_user_id==str(tg_user_id)
        )
        return results


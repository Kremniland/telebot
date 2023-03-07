from sqlalchemy import not_
from sqlalchemy.sql import func

from Project_3.database.models import Category, Film, UserGuessedFilm
from Project_3.db import get_session


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
            q = self.session.query().filter(
                not_(Film.id.in_(film_ids)),
                # !!!!что бы написать равно пишем модель.поле == атрибут
                Film.category == category_id
            ).order_by(func.random()).first() # вернет рандомно первый из списка
            return q
        else:
            # отдаст все фильмы которых нет в списке переданных film_ids
            q = self.session.query().filter(
                not_(Film.id.in_(film_ids)),
            ).order_by(func.random()).first() # вернет рандомно первый из списка
            return q


class GuessedFilmManager():

    def __init__(self):
        self.session = get_session()
        self.model = UserGuessedFilm

    def insert_guessed_film(self, tg_user_id, film_id):
        insert = UserGuessedFilm(
            tg_user_id=tg_user_id,
            film=film_id
        )
        self.session.add(insert)
        self.session.commit()

    def get_guessed_films_ids(self, tg_user_id):
        ids = self.session.query(UserGuessedFilm.film).filter(
            UserGuessedFilm.tg_user_id == tg_user_id
        )
        return ids


ses = get_session()
films=ses.query(UserGuessedFilm.film).filter(UserGuessedFilm.tg_user_id=='1494947085')

for s in films:
    print(s)

# category_id = None
# films = FilmManager().session.query(Film).filter(
#                 not_(Film.id.in_(film_ids)),
#
#             ).order_by(func.random()).first()
# print(films.name_text)



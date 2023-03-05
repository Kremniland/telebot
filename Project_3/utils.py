import csv

from database.manager import CategoryManager, FilmManager


def fill_category_data(filename):
    '''заполняем данные в категории из csv файл'''
    with open(filename, 'r', encoding='utf-8') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        # for i in rows:
        #     print(i)
        CategoryManager().insert_category(rows)


def fill_films_data(filename):
    '''заполняем данные в модель фильмы'''
    with open(filename, 'r', encoding='utf-8') as file:
        rows = csv.reader(file, delimiter=',')
        # for row in rows:
        #     print(row)
        FilmManager().insert_film(rows)


# if __name__ == '__main__':
    # fill_category_data('data_files/category_data.csv')
    # fill_films_data('data_files/emojies.csv')




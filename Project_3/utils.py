import csv

from database.manager import CategoryManager


def fill_category_data(filename):
    '''заполняем данные в категории из csv файл'''
    with open(filename, 'r') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        # for i in rows:
        #     print(i)
        CategoryManager().insert_category(rows)


# if __name__ == '__main__':
#     fill_category_data('data_files/category_data.csv')


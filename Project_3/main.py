from aiogram import executor
from sys import argv

from Project_3.utils import fill_category_data
from bot_router import dp
from init_db import create_tables
# from database.models import create_tables
# from Project_3.utils import fill_category_data


if __name__ == '__main__':
    data = argv  # сохраняем дополнительные аргументы при запуске файла
    print(data)
    # if data[1] == 'migrate': # если в команде запуска файла указать migrate то создаст таблицы
    #     create_tables() # создаем таблицы
    # elif data[1] == 'fill_category':
    #     fill_category_data('data_files/category_data.csv')  # заполнение таблицы категории из csv файла
    # elif data[1] == 'runbot'
    #     executor.start_polling(dp,
    #                        skip_updates=True)
    create_tables() # создаем таблицы
    fill_category_data('data_files/category_data.csv') # заполнение таблицы категории из csv файла
    executor.start_polling(dp,
                           skip_updates=True)


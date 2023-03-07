'''
Решить вопросы:
редис в асинхронном режиме
запуск с дополнительными параметрами
'''
from aiogram import executor
from sys import argv

from Project_3.utils import fill_category_data, fill_films_data
from bot_router import dp
from init_db import create_tables


if __name__ == '__main__':
    # data = argv  # сохраняем дополнительные аргументы при запуске файла
    # print(data)
    # if data[1] == 'migrate': # если в команде запуска файла указать migrate то создаст таблицы
    #     create_tables() # создаем таблицы
    # elif data[1] == 'fill_category':
    #     fill_category_data('data_files/category_data.csv')  # заполнение таблицы категории из csv файла
    # elif data[1] == 'fill_films':
    #     fill_films_data('data_files/emojies.csv')  # заполнение таблицы film из csv файла
    # elif data[1] == 'runbot':
    #     executor.start_polling(dp,
    #                        skip_updates=True)

    # create_tables() # создаем таблицы
    # fill_category_data('data_files/category_data.csv') # заполнение таблицы категории из csv файла
    # fill_films_data('data_files/emojies.csv')
    executor.start_polling(dp,
                           skip_updates=True)


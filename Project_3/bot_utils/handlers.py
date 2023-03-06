from aiogram import types

from Project_3.database.manager import CategoryManager, FilmManager
from Project_3.bot_utils.keyboards import get_category_btns
from Project_3.redis_client import redis_client


async def welcome_message(message: types.Message):
    text = '''
        Бот для игры. 
        Для начала отправь /start_game
    '''
    await message.answer(text=text)


async def start_game(message: types.Message):
    text = 'Выберите категорию игры:'
    user_id = message.from_user.id
    data = redis_client.get_user_data(user_id)
    if data:
        await message.answer('У вас уже начата игра. Желаете завершить игру?')
    else:
        markup = get_category_btns() # создаем клавиатуру для категорий
        await message.answer(text=text,
                             reply_markup=markup)


async def start_with_category(callback: types.CallbackQuery):
    '''обрабатываем калбэк при выборе категорий создаем данные игры
    для пользователя и помещаем их в редис'''
    user_tg_id = 1494947085
    # user_data = redis_client.get_user_data(callback.message.chat.id)
    user_data = redis_client.get_user_data(user_tg_id)
    if user_data:
        text = '''
            У вас имеется активная игра, завершите чтобы выбрать новую категорию        
        '''
        await callback.message.answer(text)
    else:
        choice = str(callback.data).split('_')[1] # id категории
        data = {
            'level_choice': choice,
            'test': 'test',
        }
        # user_tg_id = callback.message.from_user.id
        redis_client.cache_user_data(user_tg_id, data) # сохраняем в редис
        await callback.message.answer('Вы выбрали категорию')


async def finish_game(message: types.Message):
    user_id = message.from_user.id
    redis_client.delete_user_data(user_id)
    await message.answer('Игра удалена!')
    await message.answer('Колличество угаданных фильмов: 0')


async def get_movie(message: types.Message):
    films = FilmManager().get_films()
    for film in films:
        await message.answer(f'{film.emoji_text}')


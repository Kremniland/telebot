from aiogram import types
from aiogram.dispatcher import FSMContext

from Project_3.database.manager import CategoryManager, FilmManager, GuessedFilmManager
from Project_3.bot_utils.keyboards import get_category_btns
from Project_3.redis_client import redis_client
from Project_3.state import UserMessageState


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
    print(data)
    if data:
        await message.answer('У вас уже начата игра. Желаете завершить игру?')
    else:
        markup = get_category_btns() # создаем клавиатуру для категорий
        await message.answer(text=text,
                             reply_markup=markup)


async def start_with_category(callback: types.CallbackQuery, state: FSMContext):
    '''обрабатываем калбэк при выборе категорий создаем данные игры
    для пользователя и помещаем их в редис'''
    user_data = redis_client.get_user_data(callback.from_user.id)
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
        await UserMessageState.answer_text.set() # задаем состояние
        user_tg_id = callback.from_user.id
        redis_client.cache_user_data(user_tg_id, data) # сохраняем в редис

        tg_id = user_tg_id
        guessed_film = GuessedFilmManager().get_guessed_film(tg_id)  # список уже угаданных фильмов
        film = FilmManager().get_random_film(film_ids=guessed_film, category_id=choice)
        print(film.name_text)
        await callback.message.answer(film.name_text)
        await callback.message.answer(film.emoji_text)
        await callback.message.answer('Вы выбрали категорию')


async def send_questions(message: types.Message, state: FSMContext):
    tg_id = message.from_user.id
    guessed_film = GuessedFilmManager.get_guessed_film(tg_id) # список уже угаданных фильмов
    film = FilmManager()
    if not guessed_film:
        pass



async def finish_game(message: types.Message):
    user_id = message.from_user.id
    redis_client.delete_user_data(user_id)
    await message.answer('Игра удалена!')
    await message.answer('Колличество угаданных фильмов: 0')


async def get_movie(message: types.Message):
    films = FilmManager().get_random_film()
    for film in films:
        await message.answer(f'{film.emoji_text}')


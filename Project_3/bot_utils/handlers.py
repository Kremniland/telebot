from aiogram import types
from aiogram.dispatcher import FSMContext

from Project_3.database.manager import FilmManager, GuessedFilmManager
from Project_3.bot_utils.keyboards import get_category_btns
from Project_3.database.models import Film
from Project_3.redis_client import redis_client
from Project_3.bot_utils.state import UserMessageState


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
    для пользователя и помещаем их в редис, начинаем игруи выводим вопрос'''
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
        user_tg_id = callback.from_user.id
        redis_client.cache_user_data(user_tg_id, data) # сохраняем в редис

        guessed_film = GuessedFilmManager().get_guessed_film(user_tg_id)  # список уже угаданных фильмов
        # достаем фильм из выбранной категории который еще пользователь не угадывал
        film = FilmManager().get_random_film(film_ids=guessed_film, category_id=choice)
        await callback.message.answer('Вы выбрали категорию. Игра началась...')
        await callback.message.answer(f'{film.emoji_text}')
        await UserMessageState.answer_text.set()  # означает что следующее сообщение будет сохранено в state


async def send_questions(message: types.Message, state: FSMContext):
    '''обрабатываем ответ на вопрос о фильме, если он текст, сохраняем ответ в хранилище'''
    async with state.proxy() as data: # сохраняем в хранилище ответ пользователя
        data['answer_text'] = message.text
    print('Ответ:', data['answer_text'])
    user_tg_id = message.from_user.id
    await state.finish()


async def finish_game(message: types.Message):
    '''окончание игры удаление данных из редис'''
    user_id = message.from_user.id
    redis_client.delete_user_data(user_id)
    await message.answer('Игра удалена!')
    await message.answer('Колличество угаданных фильмов: 0')


async def get_movie(message: types.Message):
    films = FilmManager().session.query(Film).all()
    for film in films:
        await message.answer(f'{film.emoji_text}')


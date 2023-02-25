'''
Телеграм бот главное меню, инлайн клавиатура для фото с выбором следующего фото и лайками
сделано через глобальные переменные:
Выбор следующего фото сделано через костыли
Лайки сделаны через костыли
'''
from aiogram import types, executor, Bot, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

import random

from config import TOKEN
from keyboards import kb, ikb, kb_photo

bot = Bot(TOKEN)
dp = Dispatcher(bot)

HELP_COMMAND = '''
<b> /help </b> - <em> Help </em>
<b> /description </b> - <em> Description </em>
<b> /photo </b> - <em> Photo </em>
'''
PHOTO_LST = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZo1bZyDj2jr1hDC28Iqcha48KexDIzRVg-RxoJr1heA&s',
    'https://static-cse.canva.com/blob/847064/29.jpg',
    'https://www.istockphoto.com/resources/images/PhotoFTLP/998044806.jpg'
]
# Формируем словарь: описание к фото из списка фотографий
PHOTOS = dict(zip(PHOTO_LST, ['Фото 1', 'Фото 2', 'Фото 3']))
random_photo = random.choice(list(PHOTOS.keys()))
flag = False

async def on_startup(_):
    print('Start Bot')

async def random_photo_foo(message:types.Message):
    random_photo = random.choice(list(PHOTOS.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=PHOTOS[random_photo],
                         reply_markup=ikb)

@dp.message_handler(Text(equals='Random photo'))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Для отправки фото нажмите - Рандом фото',
                         reply_markup=kb_photo)
    await message.delete()


@dp.message_handler(Text(equals='Рандом фото'))
async def send_random_photo(message: types.Message):
    await message.answer(text='Рандомная фотка',
                         reply_markup=ReplyKeyboardRemove())
    await random_photo_foo(message)
    await message.delete()


@dp.message_handler(Text(equals='Главное меню'))
async def open_kb(message: types.Message):
    await message.answer(text='Добро пожаловать в главное меню',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Добро пожаловать!',
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_cmd(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_cmd(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Бот отправляет фото')
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAEH4WFj-ImB_utm9MxUP2dAgvh1zkQ1QgACYgMAAm2wQgOZk6ig1YUjNS4E')
    await message.delete()


@dp.message_handler(commands=['location'])
async def photo_cmd(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            longitude=random.randint(0, 50),
                            latitude=random.randint(0,50)
                            )
    await message.delete()


@dp.callback_query_handler()
async def callback_photo_random(callback: types.CallbackQuery):
    global random_photo
    global flag
    if callback.data == 'like':
        if not flag:
            await callback.answer('Вам понравилось')
            # await callback.message.answer('Вам понравилось')
            flag = True
        else:
            await callback.answer('Вы уже лайкали!')
    elif callback.data == 'dislike':
        await callback.answer('Вам не понравилось')
        # await callback.message.answer('Вам не понравилось')
    elif callback.data == 'main':
        await callback.message.answer(text='Вы в главном меню!',
                                      reply_markup=kb)
        await callback.message.delete()
        await callback.answer()
    else:
        # костылем убираем что бы новое фото != тому которое сейчас есть
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(PHOTOS.keys()))))
        # Выведет новое фото на месте предидущего
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type='photo',
                                                           caption=PHOTOS[random_photo]),
                                          reply_markup=ikb)
        await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

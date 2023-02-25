from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/vote')
kb.add(b1, b2)

async def on_startup(_):
    print('Start Bot')

@dp.message_handler(commands=['start'])
async def send_kb(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Hello',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text='👍',
                              callback_data='like')
    b2 = InlineKeyboardButton(text='👎',
                              callback_data='dislike')
    ikb.add(b1, b2)
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://zamanilka.ru/wp-content/uploads/2021/11/fantasy.jpg',
                         caption='Нравится тебе это фото?',
                         reply_markup=ikb)

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    '''функция для обработки callback_data полученных в ф-ии vote_command'''
    if callback.data == 'like':
        await callback.answer(text='Фото понравилось')
    await callback.answer(text='Фото отстой!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


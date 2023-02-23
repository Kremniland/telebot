from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='You Tube', url='https://www.youtube.com')
ib2 = InlineKeyboardButton(text='Google', url='https://www.google.com')
ikb.add(ib1).insert(ib2)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/links')
kb.add(b1)

async def on_startup(_):
    print('Start Bot')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Начало работы',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['links'])
async def links_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Куда перейти?',
                           reply_markup=ikb)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


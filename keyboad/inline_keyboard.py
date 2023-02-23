from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)  # row_width сколько кнопок в столбце

ib1 = InlineKeyboardButton(text='Button 1',
                           url='https://www.youtube.com/')
ib2 = InlineKeyboardButton(text='Button 2',
                           url='https://www.youtube.com/')

ikb.add(ib1, ib2)


@dp.message_handler(commands=['start'])
async def send_kb(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Hello word',
                           reply_markup=ikb)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

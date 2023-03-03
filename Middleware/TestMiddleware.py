from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


class CustomMiddleware(BaseMiddleware):
    '''название методов должно соблюдаться'''
    async def on_pre_process_update(self, update: types.Update, data: dict):
        print('update: ', update)
        print('pre-process update!')

    async def on_process_update(self, update: types.Update, data: dict):
        print('process update!')

    async def on_process_message(self, message: types.Message, data: dict):
        print('data: ', data)
        print('message: ', message)
        print('process message!')


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton('test', callback_data='test')],
    ])
    await message.reply('Написана коменда старт!',
                        reply_markup=ikb)
    print('Start!')


if __name__ == '__main__':
    dp.middleware.setup(CustomMiddleware())
    executor.start_polling(dp,
                           skip_updates=True)

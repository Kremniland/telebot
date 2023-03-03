'''
Middleware проверяет если message.from_user.id != my_id
то хендлеры не работают
'''
from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

my_id = 1494947085


class CustomMiddleware(BaseMiddleware):
    '''бот будет работать только если message.from_user.id = my_id'''
    async def on_process_message(self, message: types.Message, data: dict):
        if message.from_user.id != my_id:
            raise CancelHandler() # данное исключение остановит дальнейшую обработку message


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

'''
Делаем декоратор который присваивает хендлеру аттрибут key и потом проверяем
этот атрибут в middleware on_process_message
'''
from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler, current_handler

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

my_id = 1494947085


def set_key(key: str = None):
    '''добавим handler атрибут key'''
    def decorator(func):
        setattr(func, 'key', key) # добавим ф-ии атрибут key=key
        return func
    return decorator


class AdminMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get() # получили текущий хэндлер для данного события
        if handler: # если хэндлер существует
            key = getattr(handler, 'key', 'Такого атрибута нет') # получаем key от handler
            print(key)


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply('Написана коменда старт!')


@dp.message_handler(lambda message: message.text.lower() == 'привет')
@set_key('hello!') # присвоим key=hello
async def text_hello(message: types.Message):
    await message.reply('И тебе привет!')


if __name__ == '__main__':
    dp.middleware.setup(AdminMiddleware())
    executor.start_polling(dp,
                           skip_updates=True)

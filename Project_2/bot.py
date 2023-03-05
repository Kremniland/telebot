'''
Бот с антифлудом 5 сек через мидлеваре,
с валидацией емаил
'''
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from filters import EmailChek
from middlewares import ThrottlingMiddleware
from config import TOKEN


storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(EmailChek())
async def check_mail(message: types.Message):
    await message.answer('Емаил прошел фильтр!')


@dp.message_handler()
async def just_text(message: types.Message):
    await message.answer('Okay!')


if __name__ == '__main__':
    dp.middleware.setup(ThrottlingMiddleware())
    executor.start_polling(dp,
                           skip_updates=True)


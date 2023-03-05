from aiogram import Bot, executor, Dispatcher, types

from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)
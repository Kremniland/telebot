from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text='Привет Лена') # означает написать сообщение


if __name__ == '__main__':
    executor.start_polling(dp)


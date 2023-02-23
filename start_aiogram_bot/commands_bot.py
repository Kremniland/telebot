from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

COUNT = 0

HELP_COMMAND = '''
/help список команд
/start начать работу с ботом
/description описание бота
'''

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def help_commands(message: types.Message):
    await message.reply(text=HELP_COMMAND) # ответить на сообщение

@dp.message_handler(commands=['start'])
async def help_commands(message: types.Message):
    await message.answer(text='Start Bot')
    await message.delete()

@dp.message_handler(commands=['description'])
async def help_commands(message: types.Message):
    await message.reply(text='Простой бот с парой команд и выводом колличества отправленных сообщений') # ответить на сообщение
    await message.delete()

@dp.message_handler(commands=['count'])
async def check_count_message(message: types.Message):
    global COUNT
    await message.answer(f'COUNT: {COUNT}')
    COUNT += 1

if __name__ == '__main__':
    executor.start_polling(dp)


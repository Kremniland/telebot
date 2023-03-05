from aiogram import Bot, executor, Dispatcher, types

from Project_3.bot_utils.handlers import welcome_message
from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)


dp.register_message_handler(welcome_message, commands=['start'])


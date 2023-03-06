from aiogram import Bot, executor, Dispatcher, types

from Project_3.bot_utils import handlers
from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)


dp.register_message_handler(handlers.welcome_message, commands=['start'])
dp.register_message_handler(handlers.start_game, commands=['start_game'])
dp.register_message_handler(handlers.finish_game, commands=['finish_game'])

# Callback buttons handlers

dp.register_callback_query_handler(handlers.start_with_category,
                                   lambda c: str(c.data).startswith('category_'))


from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from Project_3.bot_utils import handlers
from Project_3.bot_utils.state import UserMessageState
from config import TOKEN


storage = MemoryStorage()

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)


dp.register_message_handler(handlers.welcome_message, commands=['start'])
dp.register_message_handler(handlers.start_game, commands=['start_game'])
dp.register_message_handler(handlers.finish_game, commands=['finish_game'])
# dp.register_message_handler(handlers.send_questions, content_types=['text'], state=UserMessageState.answer_text)
dp.register_message_handler(handlers.send_questions)

# Callback buttons handlers

dp.register_callback_query_handler(handlers.start_with_category,
                                   lambda c: str(c.data).startswith('category_'))


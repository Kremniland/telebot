'''
переопределяем метод check из класса Filter
для валидации емаил
'''
from aiogram import Bot, executor, Dispatcher, types
import re
from aiogram.dispatcher.filters import Filter

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


class EmailChek(Filter):
    key = 'is_email'
    pattern: str = re.compile(r'[\w.-]+@[\w-]+\.(com|ru|)')

    async def check(self, message: types.Message) -> bool:
        return self.pattern.match(message.text)


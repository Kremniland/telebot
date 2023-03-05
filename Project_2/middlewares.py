import asyncio
from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled # антифлуд
from aiogram.dispatcher.handler import CancelHandler # отменить какое либо сообщение
from aiogram.dispatcher.handler import current_handler # для получение переменных из метода get

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: int = 5):
        BaseMiddleware.__init__(self)
        self.rate_limit = limit # 5 секунд для повторной отправки

    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get() # присвоили текущий хэндлер
        dp = Dispatcher.get_current()
        try:
            await dp.throttle(key='antiflood_message', rate=self.rate_limit) # встроенный метод позволяет установить проверку на антифлуд
        except Throttled as _t:
            await self.message_throttle(message, _t)
            raise CancelHandler() # если будет флуд отменим диалог

    async def message_throttle(self, message: types.Message, throttled: Throttled):
        delta = throttled.rate -throttled.delta
        if throttled.exceeded_count <= 2:
            await message.reply('Остынь')
        await asyncio.sleep(delta)

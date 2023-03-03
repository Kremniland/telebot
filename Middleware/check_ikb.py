'''
Нажатие на кнопку вызванной инлайн клавиатуры может тот
кто вызвал сообщение с инлайн клавиатурой
'''
from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler, current_handler

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

my_id = 1494947085


class CheckMiddleware(BaseMiddleware):
    async def on_process_callback_query(self, callback: types.CallbackQuery, data: dict):
        callback_id = callback.data[callback.data.find('_')+1:] # тот кто вызвал клавиатуру
        if callback_id != str(callback.from_user.id): # callback.from_user.id тот кто нажал на кнопку
            raise CancelHandler() # если нажавший на кнопку не тот кто вызвал клавиатуру то исключение


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton('Тестовая кнопка', callback_data=f'check_{message.from_user.id}')]
    ])
    await message.answer('Тестовое сообщение',
                         reply_markup=ikb)


@dp.callback_query_handler(lambda callback: callback.data.startswith('check_'))
async def cb_check(callback: types.CallbackQuery):
    await callback.message.answer('Ты нажал на кнопку')


if __name__ == '__main__':
    dp.middleware.setup(CheckMiddleware())
    executor.start_polling(dp,
                           skip_updates=True)

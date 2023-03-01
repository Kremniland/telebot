'''
Создаем в отдельной функции инлайн клавиатуру вызываем ее командой start, объявляем глобальную переменную number,
обрабатываем в callback функции нажатие именно этой клавиатуры, изменяем number и редактируем текст сообщения
'''
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

number = 0


def get_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Increase', callback_data='btn_increase'),
         InlineKeyboardButton(text='Decrease', callback_data='btn_decrease')],
    ])
    return ikb


async def on_startup(_):
    print('Start!')


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message) -> None:
    global number
    await message.answer(f'The current number = {number}',
                         reply_markup=get_inline_keyboard())


@dp.callback_query_handler(
    lambda callback_query: callback_query.data.startswith('btn'))  # Обработает только запросы начинающиеся с btn
async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
    global number
    if callback.data == 'btn_increase':
        number += 1
        await callback.message.edit_text(f'The current number = {number}',
                                         # Изменит текст в сообщении а не выведет в новом
                                         reply_markup=get_inline_keyboard())  # чтобы клавиатура не исчезала
    elif callback.data == 'btn_decrease':
        number -= 1
        await callback.message.edit_text(f'The current number = {number}',
                                         # Изменит текст в сообщении а не выведет в новом
                                         reply_markup=get_inline_keyboard())  # чтобы клавиатура не исчезала


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

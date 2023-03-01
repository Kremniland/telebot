'''
Создаем 2 шаблона CallbackData для нажатия на кнопку для одного сообщения и
для like/dislike фото
'''
from aiogram import Bot, Dispatcher, types, executor
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

cb = CallbackData('ikb', 'action') # создаем шаблон на основе которого будем генерировать callback_data
cb_1 = CallbackData('ikb_1', 'like')

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Button', callback_data=cb.new('push'))] # создаем название действия cb.new('push')
])

ikb_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Like', callback_data=cb_1.new('like')), InlineKeyboardButton('Dislike', callback_data=cb_1.new('dislike'))],
])

async def on_startup(_):
    print('Started Bot')


@dp.message_handler(commands='start')
async def start_cmd(message: types.Message) -> None:
    await message.answer(text='Text',
                         reply_markup=ikb)


@dp.message_handler(commands='photo')
async def photo_cmd(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://avatars.mds.yandex.net/i?id=ec8eecc81cf764a8709b601d3e3716e95b2da6a2-7698965-images-thumbs&n=13',
                         reply_markup=ikb_1)


@dp.callback_query_handler(cb.filter()) # будет генерировать данные только шаблона cb
async def callback_query_handler(callback: types.CallbackQuery, callback_data: dict) -> None:
    if callback_data['action'] == 'push': # если в шаблоне action действие push то выполняем далее код
        await callback.answer('Something!')


@dp.callback_query_handler(cb_1.filter())
async def cb_photo_handler(callback: types.CallbackQuery, callback_data: dict) -> None:
    if callback_data['like'] == 'like':
        await callback.answer('You like photo!')
    if callback_data['like'] == 'dislike':
        await callback.answer('You dislike photo!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

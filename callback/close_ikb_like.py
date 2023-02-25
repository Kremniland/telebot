from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)

is_voted = False

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='👍', callback_data='like'), InlineKeyboardButton(text='👎', callback_data='dislike')],
    [InlineKeyboardButton(text='Close keyboard?', callback_data='close')]
])


async def on_startup(_):
    print('Started Bot')


@dp.message_handler()
async def start_cmd(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://wl-adme.cf.tsp.li/resize/728x/jpg/453/a87/8353725363894d8c91b554719d.jpg',
                         caption='Нравится?',
                         reply_markup=ikb)


@dp.callback_query_handler(text='close')
async def close_ikb(callback: types.CallbackQuery):
    await callback.message.delete()


@dp.callback_query_handler()
async def like_ikb(callback: types.CallbackQuery):
    global is_voted
    if not is_voted:
        if callback.data == 'like':
            is_voted = True
            await callback.answer(show_alert=False,
                                  text='Тебе понравилось')
        if callback.data == 'dislike':
            is_voted = True
            await callback.answer(show_alert=False,
                                  text='Тебе не понравилось')
    await callback.answer(show_alert=True,
                          text='Ты уже глосовал')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


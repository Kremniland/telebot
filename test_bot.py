from Project_3.redis_client import redis_client
from config import TOKEN
from aiogram import Dispatcher, Bot, executor, types


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd(message: types.Message):
    user_id = message.from_user.id
    await message.answer('привет '+str(user_id),
                         reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[
                             [types.InlineKeyboardButton('start', callback_data='start')]
                         ]))


@dp.callback_query_handler()
async def cb_start(callback: types.CallbackQuery):
    print(callback.from_user.id)
    await callback.message.answer('start!')



if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)
    # key = 1234567
    # data = {'level_choice': '777', 'test': 'test'}
    #
    # redis_client.cache_user_data(user_tg_id=key, data=data)
    #
    # print(redis_client.client.hgetall(str(key)))

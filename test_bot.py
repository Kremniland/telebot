from Project_3.redis_client import redis_client
from config import TOKEN
from aiogram import Dispatcher, Bot, executor, types


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd(message: types.Message):
    await message.answer('привет')
    user_id = message.from_user.id
    data = {'level_choice': '77765432', 'test': 'test'}
    redis_client.cache_user_data(user_id, data)
    print(user_id)
    print(redis_client.get_user_data(user_id))



if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)
    # key = 1234567
    # data = {'level_choice': '777', 'test': 'test'}
    #
    # redis_client.cache_user_data(user_tg_id=key, data=data)
    #
    # print(redis_client.client.hgetall(str(key)))

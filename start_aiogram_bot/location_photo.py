from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

HELP_MESSAGE = '''
<b> /start </b> - <em> Start </em>
<b> /help </b> - <em> Help </em>
<b> /картина </b> - <em> Начало нашей работы </em>
'''


@dp.message_handler(commands='help')
async def help_message(message: types.Message):
    # await bot.send_message(chat_id=message.chat.id, text='Hello!') # ответитт в тот чат где получил сообщение
    await bot.send_message(chat_id=message.from_user.id, text=HELP_MESSAGE,
                           parse_mode='HTML')  # ответит в личку пользователю
    await message.delete()


@dp.message_handler(commands='картинка')
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://avatars.mds.yandex.net/i?id=ec8eecc81cf764a8709b601d3e3716e95b2da6a2-7698965-images-thumbs&n=13')
    await message.delete()


@dp.message_handler(commands='location')
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=55,
                            longitude=71)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

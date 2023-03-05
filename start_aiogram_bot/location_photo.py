'''
команда help
команда вывести фото по URL
команда сделать скриншот сохранить фото и вывести сохраненное фото
'''
from aiogram import Bot, Dispatcher, types, executor
import os
import secrets
from PIL import ImageGrab

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
                         photo='https://avatars.mds.yandex.net/i?id=ec8eecc81cf764a8709b601d3e3716e95b2da6a2-7698965-images-thumbs&n=13',
                         caption='Нравится тебе это фото?')
    await message.delete()


@dp.message_handler(commands='location')
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=55,
                            longitude=71)
    await message.delete()


@dp.message_handler(commands='screen')
async def send_image(message: types.Message):
    img = ImageGrab.grab() # делает скриншот
    if not os.path.exists('static'): # если нет такой директории создаем
        os.mkdir('static')
    os.chdir('static') # переходим в static
    img_name = secrets.token_hex(8) # формируем 16тиричную строку = 8 байт
    img.save(img_name+'.png', format='PNG')
    await message.answer_photo(photo=open(img_name+'.png', 'rb'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

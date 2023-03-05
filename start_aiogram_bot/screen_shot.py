'''
команда сделать скриншот сохранить фото в папку статик,
если папки нет то создаст,
и вывести сохраненное фото
'''
from aiogram import Bot, Dispatcher, types, executor
import os
import secrets
from PIL import ImageGrab

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='screen')
async def send_image(message: types.Message):
    img = ImageGrab.grab() # делает скриншот
    if not os.path.exists('static'): # если нет такой директории создаем
        os.mkdir('static')
    os.chdir('static') # переходим в static
    img_name = secrets.token_hex(8) # формируем 16тиричную строку = 8 байт
    img.save(img_name+'.png', format='PNG')
    await bot.send_photo(chat_id=message.chat.id,
                        photo=open(img_name+'.png', 'rb'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

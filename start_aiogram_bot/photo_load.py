'''
копируем фото из чата и сохраняем в файл
'''
import secrets
from aiogram import Bot, executor, Dispatcher, types
import requests
import os
import io
from PIL import Image, ImageFilter

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

URI_INFO = f'https://api.telegram.org/bot{TOKEN}/getFile?file_id='
URI = f'https://api.telegram.org/file/bot{TOKEN}/'


@dp.message_handler(content_types=['photo'])
async def process_photo(message: types.Message):
    print(message.photo)
    file_id = message.photo[3].file_id # берем фото самого большого разрешения
    resp = requests.get(url=URI_INFO+file_id) # делаем запрос для получения img_path
    img_path = resp.json()['result']['file_path'] # получаем из запроса img_path
    img = requests.get(URI+img_path) # получаем само фото
    img = Image.open(io.BytesIO(img.content))
    img = img.filter(ImageFilter.GaussianBlur(radius=20))
    if not os.path.exists('static'):
        os.mkdir('static')
    img.save(f'static/{secrets.token_hex(8)}.png', format='PNG')


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)

# Создаем объект клавиатуры
kb = ReplyKeyboardMarkup(resize_keyboard=True, # подстраивает клавиатуру под графический интерфейс пользователя
                         # one_time_keyboard=True # default=False клавиатура сворачивается после нажатия клавиши
                         )
# Делаем кнопку клавиатуры
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/photo')
# выведет клавиши в клавиатуре add - в колонки, insert - в один ряд
kb.add(b1).add(b2).insert(b3)

HELP_COMMAND =  '''
<b> /start </b> - <em> Start </em>
<b> /help </b> - <em> Help </em>
<b> /description </b> - <em> Description </em>
<b> /photo </b> - <em> Photo </em>
'''

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML',
                           # reply_markup=ReplyKeyboardRemove() # Удалит клавиатуру после нажатия клавиши
                           )
    await message.delete()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать!',
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Наш бот может отправлять фото',
                           parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                           photo='https://appleinsider.ru/wp-content/uploads/2021/02/avatarifys.jpg')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


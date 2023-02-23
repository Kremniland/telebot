from aiogram import Bot, Dispatcher, types, executor
from  aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN


HELP_COMMAND =  '''
<b> /start </b> - <em> Start </em>
<b> /help </b> - <em> Help </em>
<b> /description </b> - <em> Description </em>
<b> /photo </b> - <em> Photo </em>
'''

bot = Bot(TOKEN)
dp =Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)

kb.add(KeyboardButton('/help')).insert(KeyboardButton('/description')).add(KeyboardButton('❤️')).insert(KeyboardButton('/orange'))

async def on_startup(_):
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Добро пожаловать!',
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Description Bot')
    await message.delete()

@dp.message_handler(commands=['orange'])
async def send_orange(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfQkjC_IRAfi8cIBT4jOAm6MJszpbCfkY_NUtpC-w&s')
    await message.delete()

@dp.message_handler()
async def send_sticker(message: types.Message):
    if message.text == '❤️':
        await bot.send_sticker(chat_id=message.from_user.id,
                               sticker='CAACAgIAAxkBAAEH2nNj9g2bDRltMrgOT9cL1Vjfbl81WwACAQADwDZPExguczCrPy1RLgQ')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

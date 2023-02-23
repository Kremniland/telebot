from aiogram import Bot, Dispatcher, types, executor

from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    '''выполняется при запуске бота'''
    print('Бот запущен!')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    '''Используем парсер для сообщения например HTML'''
    await message.answer('<em>Привет, <b>добро</b> пожаловать!</em>', parse_mode='HTML')

@dp.message_handler(commands=['give'])
async def start_command(message: types.Message):
    '''отправляем стикер в ответ, стикер получаем у бота телеграмм Get Sticker ID'''
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEH2nNj9g2bDRltMrgOT9cL1Vjfbl81WwACAQADwDZPExguczCrPy1RLgQ')

@dp.message_handler()
async def emoji_send(message: types.Message):
    await message.reply(message.text + '❤️')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)



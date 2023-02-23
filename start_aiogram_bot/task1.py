from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Я запустился')

@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    '''отправит в ответ ID отправленного стикера'''
    await message.answer(message.sticker.file_id)

# @dp.message_handler()
# async def count(message: types.Message):
#     '''отправит колличество букв а в сообщении'''
#     await message.answer(text=str(message.text.count('a')))

# @dp.message_handler(commands='give')
# async def task_1(message: types.Message):
#     await message.answer(text='Смотри какой смешной котик' + '❤️')
#     await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEH2nNj9g2bDRltMrgOT9cL1Vjfbl81WwACAQADwDZPExguczCrPy1RLgQ')

# @dp.message_handler()
# async def task_1(message: types.Message):
#     if message.text == '❤️':
#         await message.answer(text='🖤')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

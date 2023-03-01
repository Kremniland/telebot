import hashlib
from aiogram import Bot, Dispatcher, types, executor
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

user_data = ''


async def on_startup(_):
    print('Started Bot')


@dp.message_handler(commands='start')
async def start_cmd(message: types.Message) -> None:
    await message.answer(text='Введите число: ')


@dp.message_handler()
async def text_handler(message: types.Message) -> None:
    global user_data
    user_data = message.text
    await message.reply('Ваши данные сохранены')


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Echo'
    result_id = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(f'<b>{text}</b> - {user_data}',
                                            parse_mode='html')

    item = InlineQueryResultArticle(
        id=result_id,
        input_message_content=input_content,
        title='Echo Bot',
        description='Я не простой Бот'
    )

    await bot.answer_inline_query(results=[item],
                                  inline_query_id=inline_query.id,
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

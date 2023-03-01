import hashlib
from aiogram import Bot, Dispatcher, types, executor
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Started Bot')

# InlineQuery handlers

@dp.inline_handler() # обрабатывает INlineQuery запрос от API telegram
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Echo' # Получаем текст от пользователя из inline_query
    input_content = InputTextMessageContent(text) # формируем контент ответного сообщения
    result_id = hashlib.md5(text.encode()).hexdigest() # формируем уникальный идентификатор результата для API telegram необходимо
    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title='Echo!!!'
    )
    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

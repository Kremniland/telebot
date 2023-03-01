import uuid
from aiogram import Bot, executor, Dispatcher, types

from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_article(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Empty'
    input_content_bold = types.InputTextMessageContent(message_text=f'*{text}*',
                                                       parse_mode='markdown')
    input_content_italic = types.InputTextMessageContent(message_text=f'_{text}_',
                                                       parse_mode='markdown')
    item_1 = types.InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        input_message_content=input_content_bold,
        title='Жирным',
        description=text,
        thumb_url='https://cdn-icons-png.flaticon.com/512/88/88393.png?w=360'
    )
    item_2 = types.InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        input_message_content=input_content_italic,
        title='Наклонный',
        description=text,
        thumb_url='https://lumpics.ru/wp-content/uploads/2017/02/Naklon-teksta-v-Fotoshope.png'
    )
    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item_1, item_2],
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)

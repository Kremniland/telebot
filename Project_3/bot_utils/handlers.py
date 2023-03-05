from aiogram import types

from Project_3.database.manager import CategoryManager

async def welcome_message(message: types.Message):
    categories = CategoryManager().get_all_categories()
    markup = types.InlineKeyboardMarkup(width=1)
    for category in categories:
        markup.add(
            types.InlineKeyboardButton(category.name, callback_data=f'category_{category.id}')
        )
    await message.answer(text='Выбери категорию:',
                         reply_markup=markup)

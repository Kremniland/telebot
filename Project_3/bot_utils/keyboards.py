from aiogram import types

from Project_3.database.manager import CategoryManager


def get_category_btns():
    '''возвращает клавиатуру для категорий'''
    categories = CategoryManager().get_all_categories()
    markup = types.InlineKeyboardMarkup(width=1)
    for category in categories:
        markup.add(
            types.InlineKeyboardButton(category.name, callback_data=f'category_{category.id}')
        )
    markup.add(
        types.InlineKeyboardButton('Смешанный', callback_data='category_all')
    )
    return markup


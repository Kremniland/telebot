from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup,KeyboardButton

# Клавиатура для команды start
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='Random photo')
b3 = KeyboardButton(text='/description')
b4 = KeyboardButton(text='/location')
kb.add(b1, b2).add(b3, b4)

# клавиатура для команды photo
kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
b1_photo = KeyboardButton(text='Рандом фото')
b2_photo = KeyboardButton(text='Главное меню')
kb_photo.add(b1_photo, b2_photo)

# inlinekeyboard к фото
ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Y',
                           callback_data='like')
ib2 = InlineKeyboardButton(text='N',
                           callback_data='dislike')
ib3 = InlineKeyboardButton(text='Следующее фото',
                           callback_data='next')
ib4 = InlineKeyboardButton(text='Главное меню',
                           callback_data='main')
ikb.add(ib1, ib2).add(ib3).add(ib4)


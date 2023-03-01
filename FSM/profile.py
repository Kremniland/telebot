'''
FSM photo age name description
заполнение анкеты и вывод данных в конце заполнения
'''
import uuid
from aiogram import Bot, executor, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from config import TOKEN


storage = MemoryStorage() # хранилище состояний
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)


class ProfileStatesGroup(StatesGroup):
    photo = State()
    name = State()
    age = State()
    description = State()


def get_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/create'))


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer('Создать профиль: /create',
                         reply_markup=get_kb())


@dp.message_handler(commands=['create'])
async def create_cmd(message: types.Message):
    await message.answer('Создание профиля! Отправь фото')
    await ProfileStatesGroup.photo.set() # состояние бота установленно на ожидание фото


@dp.message_handler(content_types=['photo'], state=ProfileStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id # сохраняем идентификатор фото
        await message.reply('Теперь имя')
        await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['name'] = message.text
        await message.reply('Сколько тебе лет')
        await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['age'] = message.text
        await message.reply('Расскажи о себе')
        await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.description)
async def load_desc(message: types.Message, state: FSMContext) -> None:
        async with state.proxy() as data:
            data['description'] = message.text
            print(data)
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=f"{data['name']}, {data['age']}\n{data['description']}")
        await message.reply('Анкета создана')
        await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)


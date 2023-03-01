'''
FSM фото и описание
проверка фото это или нет
есть сброс состояния
'''
import uuid
from aiogram import Bot, executor, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from config import TOKEN


storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot,
                storage=storage)


def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Start'))
    return kb


def get_cancel() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/cancel'))


class ClientStates(StatesGroup):
    '''Класс для состояний пользователей'''

    photo = State()
    desc = State()


@dp.message_handler(commands='start')
async def start_cmd(message: types.Message):
    await message.answer('Hello world',
                         reply_markup=get_kb())


@dp.message_handler(commands='cancel', state='*')
async def start_cmd(message: types.Message, state: FSMContext):
    '''сбрасывает состояние'''
    current_state = await state.get_state() # текущее состояние
    if current_state is None:
        return
    await message.reply('Отменил',
                        reply_markup=get_kb())
    await state.finish()


@dp.message_handler(Text(equals='Start', ignore_case=True), state=None)
async def start_work(message: types.Message) -> None:
    await ClientStates.photo.set()
    await message.answer('Сначала отправь нам фото',
                         reply_markup=get_cancel())


@dp.message_handler(lambda message: not message.photo, state=ClientStates.photo) # проверяем если это не фото и состояние бота фото
async def check_photo(message: types.Message):
    return await message.reply(('Это не фото!'))


@dp.message_handler(lambda message: message.photo, content_types=['photo'], state=ClientStates.photo) # проверяем если это фото и состояние бота фото
async def load_photo(message: types.Message, state: FSMContext):
    '''сохраняем идентификатор фото отправленного пользователем'''
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id # сохраняем идентификатор фото которую отправил пользователь
    await ClientStates.next() # меняем состояние на следующее
    await message.reply('Теперь отправь описание')


@dp.message_handler(state=ClientStates.desc)
async def load_desc(message: types.Message, state: FSMContext):
    '''сохраняем описание отправленного пользователем'''
    async with state.proxy() as data:
        data['desc'] = message.text # сохраняем описание
    await message.reply('Фото сохранено')

    async with state.proxy() as data:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=data['desc'])
    await state.finish() # завершаем состояние


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)

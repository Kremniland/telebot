from aiogram import types


async def welcome_message(message: types.Message):

    await message.answer('Hello!')

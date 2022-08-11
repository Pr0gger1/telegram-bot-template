from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp
from filters import IsPrivate

@dp.message_handler(IsPrivate(), CommandStart())
async def start_message(message: types.Message):
    await message.answer("Бот работает!")
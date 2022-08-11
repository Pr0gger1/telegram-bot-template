from aiogram import types

from loader import dp
from filters import IsPrivate

@dp.message_handler(IsPrivate())
async def start_message(message: types.Message):
    await message.answer("Бот работает!")
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, commands
from utils.misc import rate_limit
from filters import IsPrivate


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp(), IsPrivate())
async def bot_help(message: types.Message):
    text = [f"/{cmd} - {desc}" for cmd, desc in commands.items()]

    await message.answer('\n'.join(text))

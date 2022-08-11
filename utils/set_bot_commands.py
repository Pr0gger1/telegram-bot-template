from aiogram import types
from loader import commands


async def set_default_commands(dp):
    command_list = [types.BotCommand(cmd, desc) for cmd, desc in commands.items()]
    await dp.bot.set_my_commands(command_list)

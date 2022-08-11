from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config


bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Set the False value if the project will work in the production
# DEBUG is the variable which determines work of debugger module
DEBUG: bool = True

commands: dict = {
    "start": "description",
    "settings": "description",
    "help": "description"
}
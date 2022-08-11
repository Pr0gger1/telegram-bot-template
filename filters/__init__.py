from aiogram import Dispatcher

from .private_chat_filter import IsPrivate
from .is_group_filter import IsGroup
from .admin_filter import AdminFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)

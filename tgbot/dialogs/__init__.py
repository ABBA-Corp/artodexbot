from aiogram import Dispatcher
from aiogram_dialog import DialogRegistry
from tgbot.dialogs import order


def register_dialogs(dp: Dispatcher):
    registry = DialogRegistry(dp)
    order.setup(registry)


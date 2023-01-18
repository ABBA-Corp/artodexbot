from aiogram import Dispatcher
from aiogram_dialog import DialogRegistry
from tgbot.dialogs import category


def register_dialogs(dp: Dispatcher):
    registry = DialogRegistry(dp)
    category.setup(registry)


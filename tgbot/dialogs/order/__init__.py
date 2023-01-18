from aiogram_dialog import DialogRegistry

from .dialogs import menu


def setup(registry: DialogRegistry):
    registry.register(menu)

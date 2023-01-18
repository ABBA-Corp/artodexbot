from aiogram import Dispatcher
from tgbot.callback_data.callback_data import cb_language

from .language import language_handler


def register_query_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(language_handler, cb_language.filter())

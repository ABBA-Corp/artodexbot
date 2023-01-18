from aiogram import Dispatcher, types

from .register import get_name, get_phone
from tgbot.states.states import RegisterForm


def register_other(dp: Dispatcher) -> None:
    dp.register_message_handler(get_name, state=RegisterForm.name)
    dp.register_message_handler(
        get_phone,
        state=RegisterForm.phone_number,
        content_types=types.ContentTypes.CONTACT
    )

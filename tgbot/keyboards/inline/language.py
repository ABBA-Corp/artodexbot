from aiogram import types

from tgbot.callback_data.callback_data import cb_language
from tgbot.dto.constants import languages


def language_markup() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for language in languages:
        keyboard.insert(
            types.InlineKeyboardButton(
                text=language.language_name,
                callback_data=cb_language.new(code=language.language_code)
            )
        )
    return keyboard

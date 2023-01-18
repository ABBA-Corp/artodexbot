from aiogram import types

from tgbot.dto.constants import i18n


_ = i18n.gettext


def settings_markup() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        types.KeyboardButton(text=_('👤 Изменить имя')),
        types.KeyboardButton(text=_('🌐 Изменить язык')),
        types.KeyboardButton(text=_('📞 Изменить номер телефона')),
        types.KeyboardButton(text=_('🏠 Главное меню')),
    )

    return keyboard

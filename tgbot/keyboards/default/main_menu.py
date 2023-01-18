from aiogram import types

from tgbot.dto.constants import i18n

_ = i18n.gettext


def main_menu(**kwargs) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True
    )
    keyboard.add(
        types.KeyboardButton(text=_('📦 Категории', locale=kwargs.get('locale')))
    )
    keyboard.add(
        # types.KeyboardButton(text=_('🔍 Поиск', locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_('⏳ История заказов', locale=kwargs.get('locale')))
    )
    keyboard.add(
        types.KeyboardButton(text=_('⚙️ Настройки', locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_('📧 Социальные сети', locale=kwargs.get('locale')))
    )
    return keyboard

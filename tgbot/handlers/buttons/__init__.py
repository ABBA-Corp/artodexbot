from aiogram import Dispatcher

from .main_menu import back_menu

from tgbot.states.states import UserNameForm, UserPhoneForm
from .categories import explore_categories
from .settings import (
    settings_menu,
    edit_name,
    get_name_edit,
    edit_language,
    edit_phone,
    get_edit_phone
)
from ...dto.constants import i18n

__ = i18n.lazy_gettext


def register_buttons(dp: Dispatcher) -> None:
    dp.register_message_handler(back_menu, text=__('🏠 Главное меню'), state="*")

    dp.register_message_handler(explore_categories, text=__('📦 Категории'), state="*")

    dp.register_message_handler(settings_menu, text=__('⚙️ Настройки'), state="*")

    dp.register_message_handler(edit_name, text=__('👤 Изменить имя'), state="*")
    dp.register_message_handler(get_name_edit, state=UserNameForm.name)

    dp.register_message_handler(edit_language, text=__('🌐 Изменить язык'), state="*")

    dp.register_message_handler(edit_phone, text=__('📞 Изменить номер телефона'), state="*", content_types="contact")
    dp.register_message_handler(get_edit_phone, state=UserPhoneForm.phone)

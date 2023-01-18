from aiogram import types
from tgbot.dto.constants import i18n
from tgbot.keyboards.default.main_menu import main_menu

_ = i18n.gettext


async def back_menu(message: types.Message):
    await message.answer(
        text=_('Главное меню'),
        reply_markup=main_menu()
    )

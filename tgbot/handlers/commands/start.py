from aiogram import types

from tgbot.db.dao.holder import HolderDao
from tgbot.dto.constants import i18n
from tgbot.keyboards.default.main_menu import main_menu
from tgbot.keyboards.inline.language import language_markup

_ = i18n.gettext


async def cmd_start(
        message: types.Message,
        dao: HolderDao
) -> None:
    if await dao.user.get_user(user_id=message.from_user.id) is None:
        await message.answer(
            text='Assalomu alaykum, kerakli tilni tanlang\n'
                 'Здравствуйте, выберите необходимый язык',
            reply_markup=language_markup()
        )
    else:
        await message.answer(
            text=_('Главное меню'),
            reply_markup=main_menu()
        )


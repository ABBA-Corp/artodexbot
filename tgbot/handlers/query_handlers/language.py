from typing import Dict

from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.db.dao.holder import HolderDao
from tgbot.dto.constants import i18n
from tgbot.keyboards.default.main_menu import main_menu
from tgbot.states.states import RegisterForm

_ = i18n.gettext


async def language_handler(
        callback: types.CallbackQuery,
        callback_data: Dict[str, str],
        dao: HolderDao,
        state: FSMContext
) -> None:
    await callback.message.delete()
    language_code = callback_data.get('code')
    if await dao.user.get_user(user_id=callback.from_user.id) is None:
        await callback.message.answer(
            text=_('Введите ваше имя', locale=language_code)
        )
        await state.update_data(language_code=language_code)
        await state.set_state(RegisterForm.name)
    else:
        await dao.user.update_language(
            user_id=callback.from_user.id,
            language=language_code
        )
        await callback.message.answer(
            text=_('Главное меню'),
            reply_markup=main_menu(locale=language_code)
        )


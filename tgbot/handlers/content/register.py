from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.db.dao.holder import HolderDao
from tgbot.dto.constants import i18n
from tgbot.keyboards.default.main_menu import main_menu
from tgbot.states.states import RegisterForm


_ = i18n.gettext


async def get_name(
        message: types.Message,
        state: FSMContext
) -> None:
    data = await state.get_data()
    name = message.text
    await state.update_data(name=name)
    await message.answer(
        text=_('Отправьте номер телефона', locale=data.get('language_code')),
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(
                        text=_('📞 Поделиться номером телефона', locale=data.get('language_code')),
                        request_contact=True
                    )
                ]
            ],
            row_width=1,
            resize_keyboard=True
        )
    )
    await state.set_state(RegisterForm.phone_number)


async def get_phone(
        message: types.Message,
        state: FSMContext,
        dao: HolderDao
) -> None:
    data = await state.get_data()
    phone = message.contact.phone_number
    await dao.user.add_user(
        user_id=message.from_user.id,
        name=message.from_user.full_name,
        username=message.from_user.username,
        language=data.get('language_code'),
        phone_number=phone
    )
    await message.answer(
        text=_('Главное меню', locale=data.get('language_code')),
        reply_markup=main_menu()
    )
    await state.finish()


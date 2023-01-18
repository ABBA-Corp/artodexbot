from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.db.dao.holder import HolderDao
from tgbot.dto.constants import i18n
from tgbot.keyboards.default.main_menu import main_menu
from tgbot.keyboards.default.settings import settings_markup
from tgbot.keyboards.inline.language import language_markup
from tgbot.states.states import UserNameForm, UserPhoneForm

_ = i18n.gettext


async def settings_menu(
        message: types.Message,
        state: FSMContext
) -> None:
    await state.reset_state(with_data=True)
    await message.answer(
        text=_('Выберите пункт меню'),
        reply_markup=settings_markup()
    )


async def edit_name(message: types.Message, dao: HolderDao, state: FSMContext) -> None:
    user = await dao.user.get_user(user_id=message.from_user.id)
    await message.answer(
        text=_('👤 Ваше текущее имя: {name}\n'
               'Введите новое имя'.format(name=user.name))
    )
    await state.set_state(UserNameForm.name)


async def get_name_edit(message: types.Message, dao: HolderDao, state: FSMContext) -> None:
    name = message.text
    await dao.user.edit_user_name(user_id=message.from_user.id, name=name)
    await message.answer(
        text=_('✅ Имя успешно изменено'),
        reply_markup=main_menu()
    )
    await state.finish()


async def edit_language(message: types.Message) -> None:
    await message.answer(
        text='Kerakli tilni tanlang\n'
             'Выберите необходимый язык',
        reply_markup=language_markup()
    )


async def edit_phone(message: types.Message, dao: HolderDao, state: FSMContext) -> None:
    user = await dao.user.get_user(user_id=message.from_user.id)
    await message.answer(
        text=_('📞 Ваш текущий номер телефона: {phone}\n'
               'Введите новый номер телефона'.format(phone=user.phone_number))
    )
    await state.set_state(UserPhoneForm.phone)


async def get_edit_phone(message: types.Message, dao: HolderDao, state: FSMContext) -> None:
    phone_number = message.contact.phone_number
    await dao.user.edit_user_phone(user_id=message.from_user.id, phone=phone_number)
    await message.answer(
        text=_('✅ Номер телефона успешно обновлён'),
        reply_markup=main_menu()
    )
    await state.finish()

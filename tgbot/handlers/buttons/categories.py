from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_dialog import DialogManager, ShowMode

from tgbot.states.states import MenuForm


async def explore_categories(
        message: types.Message,
        dialog_manager: DialogManager,
        state: FSMContext
) -> None:
    await state.reset_state(with_data=True)
    await dialog_manager.start(MenuForm.category, show_mode=ShowMode.SEND)

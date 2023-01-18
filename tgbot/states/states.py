from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterForm(StatesGroup):
    name = State()
    phone_number = State()


class UserNameForm(StatesGroup):
    name = State()


class UserPhoneForm(StatesGroup):
    phone = State()


class MenuForm(StatesGroup):
    category = State()
    product = State()
    info = State()
    count = State()

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware as BaseI18nMiddleware

from tgbot.db.dao.holder import HolderDao


class I18nMiddleware(BaseI18nMiddleware):
    async def get_user_locale(self, action, data):
        dao: HolderDao = data[-1].get('dao')
        current_user = types.User.get_current()
        user = await dao.user.get_user(user_id=current_user.id)
        if user:
            return user.language
        else:
            return current_user.locale

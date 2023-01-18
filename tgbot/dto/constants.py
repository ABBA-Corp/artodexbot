from tgbot.middlewares import I18nMiddleware
from .language import Language

i18n = I18nMiddleware(domain="messages", path="tgbot/locales", default="uz")
languages = [
    Language(language_name="O'zbek", language_code="uz"),
    Language(language_name="Русский", language_code="ru"),
]

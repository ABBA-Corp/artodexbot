import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tgbot.config import load_config
from tgbot.db.factory import create_pool
from tgbot.dialogs import register_dialogs
from tgbot.handlers.buttons import register_buttons
from tgbot.handlers.commands import register_commands
from tgbot.handlers.content import register_other
from tgbot.handlers.query_handlers import register_query_handlers
from tgbot.middlewares import register_middlewares

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")
    config = load_config("bot.ini")
    pool = create_pool(config=config)
    storage = MemoryStorage()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=storage)

    register_middlewares(dp, pool)
    register_commands(dp)
    register_query_handlers(dp)
    register_buttons(dp)
    register_other(dp)
    register_dialogs(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

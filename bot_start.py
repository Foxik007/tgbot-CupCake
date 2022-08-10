import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from data_base import sqllite_db
from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.FSM.biscuit import register_biscuit
from tgbot.handlers.FSM.cake import register_cake
from tgbot.handlers.admin import register_admin
from tgbot.handlers.echo import register_echo
from tgbot.handlers.menu import register_menu
from tgbot.handlers.user import register_user
from tgbot.middlewares.db import DbMiddleware
from tgbot.handlers.FSM.cupcake import register_cupcake

logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    dp.setup_middleware(DbMiddleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)

def register_all_states(dp):
    register_cupcake(dp)
    register_cake(dp)
    register_biscuit(dp)

def register_all_handlers(dp):
    register_menu(dp)
    register_admin(dp)
    register_user(dp)
    register_echo(dp)

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    sqllite_db.sql_start()

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_states(dp)
    register_all_handlers(dp)

    # start
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

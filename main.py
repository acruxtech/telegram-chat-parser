import asyncio
import logging

from pyrogram import Client
from pyrogram.methods.utilities.idle import idle

from config import load_config
from db.pool_creater import Pool

from userbot.handlers.common import register_common_handlers

logger = logging.getLogger(__name__)
config = load_config("config.ini")


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        handlers=[
            logging.FileHandler("bot.log"),
            logging.StreamHandler()
        ]
    )
    logger.error("Starting userbot")

    pool = Pool()
    await pool.create_pool(
        database=config.db.database,
        echo=False,
    )

    app = Client("my_account", config.userbot.api_id, api_hash=config.userbot.api_hash)
    register_common_handlers(app)

    await app.start()
    await idle()
    await app.stop()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Userbot stopped!")

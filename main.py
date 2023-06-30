import asyncio
import logging

from pathlib import Path
from pyrogram import Client
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from db import create_db
from config import load_config
from db.models import BaseCommon
from db.pool_creater import create_pool

logger = logging.getLogger(__name__)


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
    config = load_config("config.ini")

    pool: sessionmaker = await create_pool(
        database=config.db.database,
        echo=False,
    )

    app = Client("my_account", config.userbot.api_id, api_hash=config.userbot.api_hash)

    try:
        await app.start()
    finally:
        await app.stop()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Userbot stopped!")

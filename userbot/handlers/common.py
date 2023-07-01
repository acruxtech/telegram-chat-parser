from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from db.services.repository import Repo, repo

from userbot.filters.chat import chat_filter
from userbot.filters.keyword import keyword_filter


@repo
async def chat_message_with_keyword_handler(client: Client, message: Message, repo: Repo):
    print(client, message, repo)


def register_common_handlers(app: Client):
    app.add_handler(
        MessageHandler(
            chat_message_with_keyword_handler, 
            # chat_filter(Repo().get_chats()),
            # keyword_filter(Repo().get_keywords())
        )
    )
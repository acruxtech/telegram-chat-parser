from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from db.services.repository import Repo, repo
from db.pool_creater import Pool
from db.models import Chat, Keyword

from userbot.filters.chat import chat_filter
from userbot.filters.keyword import keyword_filter
from userbot.types.SearchParameters import SearchParamaters


@repo
async def chat_message_with_keyword_handler(client: Client, message: Message, repo: Repo):
    print(message.text)


@repo
async def set_chats(client: Client, message: Message, repo: Repo):
    input_chats = message.text.splitlines()[1:]
    
    chats = []
    for chat_identifier in input_chats:
        chat = await client.get_chat(chat_identifier)
        new_chat = Chat(
            telegram_id=chat.id,
            title=chat.title
        )
        chats.append(new_chat)

    await repo.set_chats(chats)
    await client.send_message(
        1425820937,
        'Чаты для парсинга установлены',
        reply_to_message_id=message.id
    )


@repo
async def set_keywords(client: Client, message: Message, repo: Repo):
    input_keywords = message.text.splitlines()[1:]

    keywords = []
    for keyword in input_keywords:
        new_keyword = Keyword(
            text=keyword
        )
        keywords.append(new_keyword)

    await repo.set_keywords(keywords)
    await client.send_message(
        1425820937,
        'Ключевые слова для парсинга установлены',
        reply_to_message_id=message.id
    )


async def register_common_handlers(app: Client):
    app.add_handler(
        MessageHandler(
            chat_message_with_keyword_handler, 
            chat_filter(SearchParamaters.chats)
            # keyword_filter(SearchParamaters.keywords)
        )
    )
    app.add_handler(
        MessageHandler(
            set_chats,
            chat_filter([1425820937]) &
            keyword_filter(['!chats'])
        )
    )
    app.add_handler(
        MessageHandler(
            set_keywords,
            chat_filter([1425820937]) &
            keyword_filter(['!keywords'])
        )
    )
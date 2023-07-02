from pyrogram import filters
from pyrogram.types import Message


def chat_filter(chat_ids: list[int]):
    async def func(flt, _, message: Message):
        print(chat_ids)
        return message.chat.id in chat_ids
    
    return filters.create(func, chat_ids=chat_ids)
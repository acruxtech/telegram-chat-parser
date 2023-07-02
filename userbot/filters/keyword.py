from pyrogram import filters
from pyrogram.types import Message


def keyword_filter(keywords: list[str]):
    async def func(flt, _, message: Message):
        return all(map(lambda kw: kw in message.text, keywords))
    
    return filters.create(func, keywords=keywords)
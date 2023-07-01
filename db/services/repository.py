from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Chat, Keyword
from db.pool_creater import Pool


class Repo:
    """Db abstraction layer"""


    def __init__(self, conn):
        self.conn: AsyncSession = conn


    async def get_chats(self) -> list[Chat]:
        """Return list of all added chats

        Returns:
            list[Chat]: list of chat objects
        """
        res = await self.conn.execute(
                select(Chat)
            )

        return res.scalars().all()
    

    async def get_keywords(self) -> list[Keyword]:
        """Return list of all added keywords

        Returns:
            list[Keyword]: list of keyword objects
        """
        res = await self.conn.execute(
                select(Keyword)
            )

        return res.scalars().all()

    
    # async def update_obj(self, obj_id, **kwargs):
    #     # get obj
    #     if not obj:
    #         raise ValueError(f'Obj with id {obj_id} doesn\'t exist')

    #     for key, value in kwargs.items():
    #         if not hasattr(obj, key):
    #             raise ValueError(f'Class `Obj` doesn\'t have argument {key}') 
    #         setattr(obj, key, value)

    #     await self.conn.commit()


    async def delete_chats(self):
        for chat in self.get_chats():
            await self.conn.delete(chat)
        
        await self.conn.commit()


    async def delete_keywords(self):
        for kw in self.get_keywords():
            await self.conn.delete(kw)
        
        await self.conn.commit()


def repo(func):

    async def wrapper(*args, **kwargs):
        db: AsyncSession = Pool().get_current()
        repo = Repo(db)
        return await func(*args, repo, **kwargs)

    return wrapper
    
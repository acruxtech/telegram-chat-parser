from datetime import datetime
from typing import List
from sqlalchemy import Column, BigInteger, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship


from db.base import Base


class BaseCommon(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Chat(BaseCommon):    
    __tablename__ = "users"

    telegram_id = Column(BigInteger)
    title = Column(String)

    def __repr__(self):
        return (
            f'Chat(telegram_id={self.telegram_id}, title={self.title})'
        )


class Keyword(BaseCommon):    
    __tablename__ = "keywords"

    text = Column(String)

    def __repr__(self):
        return (
            f'Keyword(text={self.text})'
        )

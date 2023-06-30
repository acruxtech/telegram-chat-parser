import json
import configparser
from dataclasses import dataclass


@dataclass
class DbConfig:
    database: str


@dataclass
class Userbot:
    api_id: str
    api_hash: str


@dataclass
class Config:
    userbot: Userbot
    db: DbConfig


def cast_bool(value: str) -> bool:
    if not value:
        return False
    return value.lower() in ("true", "t", "1", "yes", "y")



def load_config(path: str):
    config_ = configparser.ConfigParser()
    config_.read(path)

    return Config(
        userbot=Userbot(**config_["userbot"]),
        db=DbConfig(**config_["db"]),
    )


config = load_config("config.ini")

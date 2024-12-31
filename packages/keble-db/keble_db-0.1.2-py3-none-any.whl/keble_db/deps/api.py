from typing import Generator
from pymongo import MongoClient
from qdrant_client import QdrantClient
from redis import Redis
from sqlmodel import Session

from ..session import Db


class ApiDbDeps:

    def __init__(self, db: Db):
        self.__db = db

    def get_redis(self) -> Generator[Redis | None, None, None]:
        r = None
        try:
            r = self.__db.get_redis(force_new_instance=True)
            yield r
        finally:
            self.__db.try_close(r)

    def get_mongo(self) -> Generator[MongoClient | None, None, None]:
        m = None
        try:
            m = self.__db.get_mongo(new_instance=True)
            yield m
        finally:
            self.__db.try_close(m)

    def get_write_sql(self) -> Generator[Session | None, None, None]:
        s = None
        try:
            s = self.__db.get_sql_write_client(new_instance=True)
            yield s
        finally:
            self.__db.try_close(s)

    def get_qdrant(self) -> Generator[QdrantClient | None, None, None]:
        q = None
        try:
            q = self.__db.get_qdrant_client(new_instance=True)
            yield q
        finally:
            self.__db.try_close(q)

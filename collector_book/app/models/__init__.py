import urllib.parse
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from ..config import MONGO_URL, MONGO_URL2, MONGO_DB_NAME, MONGO_PASSWORD


class MongoDB:
    def __init__(self):
        self.client = None
        self.engine = None

    def connect(self):
        uri = f"{MONGO_URL}{urllib.parse.quote_plus(MONGO_PASSWORD)}{MONGO_URL2}"
        self.client = AsyncIOMotorClient(uri)
        self.engine = AIOEngine(client=self.client, database=MONGO_DB_NAME)
        print("==== DB CONNECT !!! ====")

    def close(self):
        self.client.close()
        print("==== DB DISCONNECT !!! ===")


mongodb = MongoDB()

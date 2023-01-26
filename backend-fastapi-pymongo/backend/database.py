from pymongo import MongoClient
from config import settings

class db:
    def __init__(self, dbname: str = 'dev_db'):
        self.client = MongoClient(settings.db_uri)
        self.db = self.client[dbname]

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()

def get_client():
    return MongoClient(settings.db_uri)

def get_db(dbname: str = 'genshin'):
    client = get_client()
    try:
        yield client[dbname]
    finally:
        client.close()
import json
from database import get_client
from pymongo import InsertOne

def import_good(filename: str, collection_name: str = 'import_data', db_name: str = 'genshin'):
    client = get_client()
    db = client[db_name]
    collection = db[collection_name]
    requesting = []

    with open(r"filename") as f:
        for jsonObj in f:
            myDict = json.loads(jsonObj)
            requesting.append(InsertOne(myDict))

    result = collection.bulk_write(requesting)
    client.close()
    return result
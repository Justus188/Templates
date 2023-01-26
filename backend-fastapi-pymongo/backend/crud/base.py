'''Data Access Layer Base Class implementing CRUD operations for MongoDB

Similar to DAO pattern but called CRUD in FastAPI by convention.'''

from pymongo import CursorType
from pymongo.results import UpdateResult, DeleteResult, InsertManyResult
from bson.objectid import ObjectId
from warnings import warn

def id_to_bsonid(data: dict | None) -> dict:
    if type(data) is dict:
        if ('id' in data):
            if type(data['id']) is dict:
                if '$in' in data['id']:
                    data['_id'] = {'$in': [ObjectId(id) for id in data['id']['$in']]}
                else:
                    warn('id_to_bsonid: id dict does not contain $in key')
            else:
                data['_id'] = ObjectId(data['id'])
            del data['id']
    return data

def bsonid_to_id(data: dict | None) -> dict:
    if type(data) is dict:
        if ('_id' in data):
            if type(data['_id']) is dict:
                if '$in' in data['_id']:
                    data['id'] = {'$in': [ObjectId(id) for id in data['id']['$in']]}
                else:
                    warn('bsonid_to_id: _id dict does not contain $in key')
            else:
                data['id'] = str(data['_id'])
            del data['_id']
    elif type(data) is list:
        return map(bsonid_to_id, data)
    return data

class CRUDBase: #ie the DAO Base Class
    def __init__(self, collection: str, debug: bool = False):
        self.collection = collection
        self.debug = debug

    def log(self, operation):
        print(f'CRUD operation: {operation} on collection: {self.collection}')

    def create_one(self, db, data: dict) -> dict:
        if self.debug:
            self.log('create_one')

        result = db[self.collection].insert_one(data)
        return self.read_one(db, {'_id': result.inserted_id})

    def create(self, db, data: list) -> list:
        if self.debug:
            self.log('create')
        
        result = db[self.collection].insert_many(data)
        return self.read(db, {'_id': {'$in': result.inserted_ids}})

    def read(self, db, filter: dict = None, sort: list = None, skip: int = None, limit: int = None) -> CursorType:
        if self.debug:
            self.log('read')
        
        filter = id_to_bsonid(filter)
        return db[self.collection].find(filter).sort(sort).skip(skip).limit(limit)
    
    def read_one(self, db, filter: dict = None) -> dict | None:
        if self.debug:
            self.log('read_one')
        
        filter = id_to_bsonid(filter)
        result = db[self.collection].find_one(filter)
        if result is None:
            return None
        return bsonid_to_id({**result, 'created_at': result['_id'].generation_time})

    def read_distinct(self, db, distinct: str = 'attr_to_apply_unqiue_on', filter: dict = None) -> list:
        if self.debug:
            self.log('read_distinct')
        
        filter = id_to_bsonid(filter)
        result = db[self.collection].distinct(distinct, filter)
        return bsonid_to_id(result)

    def update(self, db, data: dict, filter = None) -> UpdateResult:
        if self.debug:
            self.log('update')

        if filter is None:
            warn('No filter provided, updating all documents in collection')
        else:
            filter = id_to_bsonid(filter)
        return db[self.collection].update_many(filter, {'$set': data})

    def delete(self, db, filter: dict = None) -> DeleteResult:
        if self.debug:
            self.log('delete')
        
        if filter is None:
            warn('No filter provided, deleting all documents in collection')
        else:
            filter = id_to_bsonid(filter)
        return db[self.collection].delete_many(filter)
from pymongo import MongoClient

class SimpleDataStore:
    def __init__(self,url= "mongodb://localhost:27017",database_name = 'appstore'):
        self.client = MongoClient(url)
        db = self.client[database_name]

    def insert_one(self, collection_name, data):
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        return result.inserted_id

    def find_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def update_one(self, collection_name, query, update):
        collection = self.db[collection_name]
        result = collection.update_one(query, {"$set": update})
        return result.modified_count

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count

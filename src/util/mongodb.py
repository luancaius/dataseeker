from pymongo import MongoClient


class MongoDb:
    _client = {}

    @staticmethod
    def get_client():
        if not MongoDb._client:
            MongoDb._client = MongoClient('mongodb://localhost:27017')
            print(MongoDb._client.server_info())

        return MongoDb._client

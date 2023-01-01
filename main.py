import sys
import requests
import redis
from src.handlers.cache_handler import CacheHandler
import json
from src.util.mongodb import MongoDb

def read_request_from_file(filename):
    return 'https://www.boredapi.com/api/activity?participants=4'


def handle_request(url):
    cache_handler = CacheHandler()
    response_cache = cache_handler.get(url)
    print('checking cache')
    if response_cache:
        print('has cache')
        return json.loads(response_cache)
    else:
        print('no cache')
        response_cache = requests.get(url).json()
        cache_handler.set(url, json.dumps(response_cache))
        return response_cache

def convert_to_dict(input):
    if isinstance(input, dict):
        return input
    else:
        print(input, type(input))
        pass

def save_to_database(data):
    print('saving to database')
    mongoclient = MongoDb.get_client()
    db = mongoclient.test
    print('db', db)
    collection = db.first
    print('collection', collection)
    collection.insert_one(data)
    print('saved')

if __name__ == "__main__":
    print('starting dataseeker')
    print(sys.argv)
    r = redis.Redis(host='localhost', port=6379, db=0)

    filename = sys.argv[1]
    url = read_request_from_file(filename)
    response = handle_request(url)

    result = convert_to_dict(response)
    save_to_database(result)


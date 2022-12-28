import redis


class CacheHandler:
    def __init__(self):
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)

    def get(self, key):
        return self.redis_client.get(key)

    def set(self, key, value):
        self.redis_client.set(key, value)
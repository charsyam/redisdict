from __future__ import with_statement
import redis

class RedisDictHash(object):
    def __init__(self, key, client):
        self.key = key
        self.client = client

    def __getitem__(self, key):
        return self.client.hget(self.key, key)

    def __setitem__(self, key, value):
        self.client.hset(self.key, key, value)

class RedisDict(object):
    def __init__(self, client):
        self.client = client

    def __getitem__(self, key):
        return self.client.get(key)

    def __setitem__(self, key, value):
        self.client.set(key, value)

    def hash(self, key):
        return RedisDictHash(key, self.client)

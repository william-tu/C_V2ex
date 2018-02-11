# -*- coding:utf-8 -*-
import redis


class RedisPipeline(object):
    def __init__(self):
        self.r = redis.Redis(connection_pool=RedisPool.get_pool())

    def set_verify_code(self, email, value):
        self.r.set(email, value, ex=60 * 60 * 30)

    def get_verify_code(self, email):
        return self.r.get(email)


class RedisPool(object):
    def __init__(self):
        self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

    @classmethod
    def get_pool(cls):
        return cls().pool

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

# -*- coding: utf-8 -*-

import os, redis
from rq import Worker, Queue, Connection
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)
if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, ['qname'])).work()
'''
@Author: John
@Date: 2020-03-02 19:31:30
@LastEditors: John
@LastEditTime: 2020-03-02 22:03:40
@Description: 
'''
import redis
import rediscluster

# For standalone use.
DUPEFILTER_KEY = 'dupefilter:%(timestamp)s'

PIPELINE_KEY = '%(spider)s:items'

REDIS_CLS = redis.RedisCluster
REDIS_ENCODING = 'utf-8'
# Sane connection defaults.
REDIS_PARAMS = {
    'socket_timeout': 30,
    'socket_connect_timeout': 30,
    'retry_on_timeout': True,
    'encoding': REDIS_ENCODING,
}

SCHEDULER_QUEUE_KEY = '%(spider)s:requests'
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'
SCHEDULER_DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

START_URLS_KEY = '%(name)s:start_urls'
START_URLS_AS_SET = False

# Defaults Bloom Filter Settings
BLOOMFILTER_HASH_NUMBER = 6
BLOOMFILTER_BIT = 30

REDIS_CLUSTER_CLS = rediscluster.RedisCluster

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import redis
import pymysql
import pymongo
import logging
from scrapy_utils.items import *
from twisted.enterprise import adbapi
from twisted.internet import reactor, defer

logger = logging.getLogger(__name__)


class DistortionSQL:

    def __init__(self, mysql_client_pool):
        self.mysql_client_pool = mysql_client_pool

    @classmethod
    def from_crawler(cls, crawler):
        """client to MySQL
        :param crawler:
        :return:
        """
        client_param = dict(
            host=crawler.settings.get('MYSQL_HOST'),
            db=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            passwd=crawler.settings.get('MYSQL_PASSWORD'),
            charset=crawler.settings.get('MYSQL_CHARSET'),
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
            cp_reconnect=True,
        )
        mysql_client_pool = adbapi.ConnectionPool("pymysql", **client_param)
        adbapi.ConnectionPool.max = crawler.settings.get("MYSQL_CONN_MAX")
        return cls(mysql_client_pool)

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        self.mysql_client_pool.close()


class DistortionMongo:

    def __init__(self, mongo_uri, mongo_db, mongo_col):
        self.client = pymongo.MongoClient(mongo_uri)
        self.mongodb = self.client[mongo_db]
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_col = mongo_col
        self.mongo_col.create_index('id', unique=True)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_col=crawler.settings.get('MONGO_COL'),
        )

    def close_spider(self, spider):
        self.client.close()


class RedisPoolClient:
    def __init__(self, REDPool):
        self.RDSPool = REDPool

    @classmethod
    def from_crawler(cls, crawler):
        REDIS_URL = crawler.settings.get("REDIS_URL")
        pool = redis.ConnectionPool.from_url(REDIS_URL)
        REDPool = redis.Redis(connection_pool=pool).pipeline(transaction=False)
        return cls(REDPool)

    def close(self, spider):
        self.RDSPool.close()


class BaiDuBaiKePipeline(DistortionSQL):

    def process_item(self, item, spider):
        if isinstance(item, ScrapyUtilsItem):
            self.mysql_client_pool.runInteraction(self.insertPaper, item)
        return item

    @staticmethod
    def insertPaper(cursor, item):
        pass


class MongoExamplePipeline(DistortionMongo):

    @defer.inlineCallbacks
    def process_item(self, item, spider):
        out = defer.Deferred()
        reactor.callInThread(self._insert, item, out, spider)
        yield out
        defer.returnValue(item)
        return item

    def _insert(self, item, out, spider):
        if isinstance(item, ScrapyUtilsItem):
            self.mongodb[self.mongo_col].insert_many(dict(item))
            reactor.callFromThread(out.callback, item)
        return item


class RedisExamplePipeline(RedisPoolClient):
    def process_item(self, item, spider):
        if isinstance(item, ScrapyUtilsItem):
            item_dict = dict(item)
            for msg in item_dict.get('detail_id'):
                self.RDSPool.sadd('WanFangJournalIdItem', msg)
            self.RDSPool.execute()
        return item

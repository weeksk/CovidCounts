# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from pymongo import MongoClient
import logging
# from ..coviddata import settings


class CoviddataPipeline:


    class MongoPipeline(object):
        collection_name = 'covid_data'

        def __init__(self, mongo_uri, mongo_db):
            self.mongo_uri = mongo_uri
            self.mongo_db = mongo_db

        @classmethod
        def from_crawler(cls, crawler):
            return cls(
                mongo_uri=crawler.settings.get('MONGO_URI'),
                mongo_db=crawler.settings.get('MONGO_DATABASE')
            )

        def open_spider(self, spider):
            self.client = pymongo.MongoClient(self.mongo_uri)
            self.db = self.client[self.mongo_db]

        def closer_spider(self, spider):
            self.client.close()

        def process_item(self, item, spider):
            self.db[self.collection_name].insert(dict(item))
            logging.debug("MongoDB updated with today's covid data")
            return item

# class CoviddataPipeline:
# def process_item(self, item, spider):
#     return item
#
# def __init__(self):
#     self.client = MongoClient(
#         "mongodb://kcweeks92:thisisatest@atlas-t81s2p-shard-0/cluster0-shard-00-00.lltxb"
#         ".mongodb.net:27017,cluster0-shard-00-01.lltxb.mongodb.net:27017,cluster0-shard"
#         "-00-02.lltxb.mongodb.net:27017/covid?ssl=true&replicaSet=atlas-t81s2p-shard-0$authSource=admin"
#     )
#     self.db = self.client.covid
#     self.collection = self.db['covid_tb']
#
#
#     # self.conn = pymongo.MongoClient(
#     #     'localhost',
#     #     81248
#     # )
#     # db = self.conn['covid']
#     # self.collection = db['coviddata_tb']
#
#
# def process_item(self, item, spider):
#     self.collection.insert(dict(item))
#     return item

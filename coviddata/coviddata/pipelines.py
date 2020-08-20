# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo

class CoviddataPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient('mongodb+srv://kcweeks92:thisisatest@cluster0.lltxb.mongodb.net/covid?retryWrites=true&w=majority/ssl=True'
                                        , ssl=True)
        db = self.conn['covid']
        self.collection = db['coviddata_tb']


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
        #
        # for item in dict(item):
        #     self.collection.insert_one(item)

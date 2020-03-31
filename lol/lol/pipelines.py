# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo

class LolPipeline(object):

    def __init__(self,mongo_url,mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        mongo_url = crawler.settings.get('MONGO_URL')
        mongo_db = crawler.settings.get('MONGO_DB')
        return cls(mongo_url,mongo_db)

    def open_spider(self,spider):
        self.connect = pymongo.MongoClient(host=self.mongo_url)
        self.db = self.connect[self.mongo_db]

    def process_item(self, item, spider):
        for roles in item['roles']:
            self.db[roles].insert(dict(item))
            return item

    def close_respider(self,spider):
        self.connect.close()


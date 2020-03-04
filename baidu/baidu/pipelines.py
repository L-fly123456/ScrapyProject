# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from baidu.settings import MONGO_HOST
class BaiduPipeline(object):
    def open_spider(self,spider):
        client = MongoClient(MONGO_HOST)
        self.db = client["baidu"]["tieba"]

    def process_item(self, item, spider):
        self.db.insert(item)
        return item

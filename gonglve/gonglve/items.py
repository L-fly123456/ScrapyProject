# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhiyouxingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tag = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

class YoujiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tag = scrapy.Field()
    go_time = scrapy.Field()
    day = scrapy.Field()
    people = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    cost = scrapy.Field()

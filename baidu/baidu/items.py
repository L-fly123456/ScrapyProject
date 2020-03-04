# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    title= scrapy.Field()
    href = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    content_img = scrapy.Field()


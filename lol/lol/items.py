# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class LolItem(scrapy.Item):
    # define the fields for your item here like:

    roles = scrapy.Field()
    hero = scrapy.Field()
    skills = scrapy.Field()
    skin_image = scrapy.Field()



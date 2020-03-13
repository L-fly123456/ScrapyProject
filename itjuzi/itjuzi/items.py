# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItjuziItem(scrapy.Item):
    # define the fields for your item here like:
    com_id = scrapy.Field()
    com_name = scrapy.Field()
    cat_name = scrapy.Field()
    sub_cat_name = scrapy.Field()
    com_logo_archive = scrapy.Field()
    com_location = scrapy.Field()
    invse_time = scrapy.Field()
    invse_money = scrapy.Field()
    money = scrapy.Field()
    com_born_time = scrapy.Field()
    team_member = scrapy.Field()
    com_des = scrapy.Field()
    com_url = scrapy.Field()



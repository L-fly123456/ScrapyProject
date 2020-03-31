# -*- coding: utf-8 -*-
import scrapy
import json
from copy import deepcopy
from  lol.items import LolItem

class HerosSpider(scrapy.Spider):
    name = 'heros'
    allowed_domains = ['lol.qq.com']
    start_urls = ['https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=29']

    def parse(self, response):
        '''
        提取索引页的英雄id,用来构造详情页xhr请求的url
        :param response: 索引页
        :return: 详情页请求对象
        '''
        base_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'
        response = json.loads(response.text)
        hero_list = response.get('hero')
        for hero in hero_list:
            heroid = hero.get('heroId')
            detail_url = base_url.format(heroid)
            yield scrapy.Request(
                detail_url,
                callback = self.detail_parse,
                dont_filter=True,
            )

    def detail_parse(self,response):
        '''
        提取详情页的信息
        :param response: 详情页
        :return: 提取到的数据
        '''
        response = json.loads(response.text)
        item = LolItem()
        hero = response.get('hero')
        # 英雄的属性，坦克----
        item['roles'] = hero.get('roles')
        # 英雄名字和称号
        item['hero'] = '---'.join([hero.get('name'),hero.get('title')])
        item['skills'] = []
        # 英雄技能描述
        for spells in response.get('spells'):
            item['skills'].append(': '.join([spells.get('name'),spells.get('description').replace('<br>','')]))
        item['skin_image'] = []
        # 英雄皮肤
        for skin in response.get('skins'):
            if skin.get('mainImg') == "":
                continue
            item['skin_image'].append('---'.join([skin.get('name'),skin.get('mainImg')]))
        yield item





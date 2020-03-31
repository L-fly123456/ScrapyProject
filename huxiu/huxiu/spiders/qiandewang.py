# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from copy import deepcopy
from huxiu.items import HuxiuItem


class QiandewangSpider(scrapy.Spider):
    name = 'qiandewang'
    allowed_domains = ['member.com','https://www.huxiu.com/article']

    def start_requests(self):
        base_url = 'https://www.huxiu.com/member/1405886/article/%d.html'
        for page in range(1,3):
            index_url = base_url%(page)
            yield scrapy.Request(
                index_url,
                dont_filter=True,
            )

    def parse(self, response):
        item = HuxiuItem()
        # le = LinkExtractor(restrict_css='div.message-box',
        #                    deny='/article\/(d+)\.html$')
        data_list = response.css('div.mob-ctt')
        for data in data_list:
            item['author'] = '钱德虎'
            item['date'] = data.css('div.mob-author span.time::text').extract_first()
            item['sub'] = data.css('div.mob-sub::text').extract_first()
            href = response.urljoin(data.css('h3 a::attr(href)').extract_first())
            # print(item)
            yield scrapy.Request(
                href,
                callback = self.detail_parse,
                dont_filter = True,
                meta={'item':deepcopy(item)}
            )

    def detail_parse(self,response):
        item = response.meta['item']
        item['title'] = response.css('h1.article__title::text').extract_first()
        content_list = response.css('div.article-wrap.auto-height').xpath('string(.)').extract()
        item['content'] = ','.join([content.replace('\xa0','')for content in content_list])
        yield item



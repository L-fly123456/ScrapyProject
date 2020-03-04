# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy



class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        item = {}
        div_list = response.xpath('//div[@class="left-menu-container"]/div[@class="menu-list"]/div')
        for div in div_list:
            item["books"] = div.xpath("./dl/dt/h3/a/text()").extract_first()
            pindao_books = div.xpath("./dl/dd")
            for pindao_book in pindao_books:
                a_list = pindao_book.xpath("./a")
                for a in a_list:
                    item["href"] = a.xpath("./@href").extract_first()
                    item["pindao_book"] = a.xpath('./text()').extract_first()
                    yield scrapy.Request(
                        item["href"],
                        callback=self.parse_book_detail,
                        meta = {"item":deepcopy(item)}
                    )

    def parse_book_detail(self,response):
        item = response.meta["item"]
        div_list = response.xpath('//div[@class="border-out"]/div[@class="border-in"]/div')

        for div in div_list:
            href = div.xpath('./div/div/a/@href').extract_first()
            item["book_href"] = response.urljoin(href)
            item["book_title"] = div.xpath('./div/div/a/@title').extract_first()
            yield item




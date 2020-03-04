# -*- coding: utf-8 -*-
import scrapy
from baidu.items import BaiduItem


class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw=%E5%A8%B1%E4%B9%90&ie=utf-8&pn=0']

    def parse(self, response):
        div_list = response.xpath('//div[@class="t_con cleafix"]/div[2]/div')
        for div in div_list:
            item = BaiduItem()
            item["author"]=div.xpath('./div[2]/span/@title').extract_first()
            item["title"]=div.xpath("./div/a/text()").extract_first()
            item["href"]=div.xpath("./div/a/@href").extract_first()
            item["time"]=div.xpath("./div[2]/span[2]/text()").extract_first()
            if item["author"] and item["title"] and item["href"] :
                item["href"] = "http://tieba.baidu.com" + item['href']
                yield scrapy.Request(
                    item["href"],
                    callback=self.parse_detail,
                    meta = item
                )
        next_url = response.xpath('//a[@class="next pagination-item "]/@href').extract_first()
        if next_url is not None:
            next_url=response.urljoin(next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def parse_detail(self,response):
        item = response.meta
        item["content"]=response.xpath('string(//div[@class="d_post_content j_d_post_content  clearfix"])').extract_first().replace(" ","")
        item["content_img"]=response.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/img/@src').extract()
        yield item




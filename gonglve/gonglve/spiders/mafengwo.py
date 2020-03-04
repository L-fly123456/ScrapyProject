# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.http import FormRequest
from scrapy.utils.project import get_project_settings
import re
from gonglve.items import ZhiyouxingItem,YoujiItem


class MafengwoSpider(scrapy.Spider):
    name = 'mafengwo'
    allowed_domains = ['www.mefengwo.cn']
    start_urls = ['http://www.mafengwo.cn/gonglve/']
    def start_requests(self):
        '''
        重写基类的start_requests方法，发送post请求
        :return: 请求对象
        '''
        MAX_PAGE = get_project_settings().get("MAX_PAGE")
        for i in range(0,MAX_PAGE):
            data = dict(page = str(i),)
            yield FormRequest(self.start_urls[0],formdata=data,method = 'POST',callback=self.parse)

    def parse(self, response):
        '''
        由于连接提取器提取到的部分链接返回的是521异常状态码，程序自动忽略，所以分两种情况讨论；
        返回521状态码的链接要加上settings里设置的cookies和headers才能返回200，cookies会失效，所以使用时要添加cookies;
        521反爬技术在我的个人博客中会讲到。
        其他链接就正常构造请求对象。
        :param response:
        :return: 请求对象
        '''
        le = LinkExtractor(restrict_css='div._j_feed_data',
                           deny='/gonglve/$')

        for link in le.extract_links(response):
            print(link.url)
            settings = get_project_settings()
            cookies = {i.split("=")[0]: i.split("=")[1] for i in settings.get("COOKIES").split("; ")}
            if '1010616' in link.url:
                yield scrapy.Request(
                    link.url,
                    callback = self.ziyouxing_parse,
                    dont_filter=True,
            )
            else:
                yield scrapy.Request(
                    link.url,
                    callback=self.youji_parse,
                    headers=settings.get("HEADERS"),
                    cookies=cookies,
                    dont_filter=True,
                )

    def youji_parse(self,response):
        '''
        加了反爬的链接
        :param response:
        :return:
        '''
        item = YoujiItem()
        item["tag"] = "游记"
        item["title"] = response.css('div.vi_con h1::text').extract_first()
        item["go_time"] = response.css('div.tarvel_dir_list.clearfix ul li.time::text').extract()[1]
        item["day"] = response.css('div.tarvel_dir_list.clearfix ul li.day::text').extract()[1]
        item["people"] = response.css('div.tarvel_dir_list.clearfix ul li.people::text').extract()[1]
        item["cost"] = response.css('div.tarvel_dir_list.clearfix ul li.cost::text').extract()[1]
        content = response.css('div._j_content_box').xpath('string(.)').extract()
        if content:
            con = "".join([i.replace(' ','').replace('\n','')for i in content])
            item["content"] = con
        yield item


    def ziyouxing_parse(self,response):
        '''
        没加反爬的链接
        :param response:
        :return:
        '''
        item = ZhiyouxingItem()
        item["tag"] = "自由行"
        item["title"] = response.css('div.l-topic h1::text').extract_first()
        content = response.css('div.p-section::text').extract()
        con = "".join([i.strip('\n ').replace('xa0','')for i in content])
        item['content'] = con
        yield item

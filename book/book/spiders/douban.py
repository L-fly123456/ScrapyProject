# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from book.items import DoubanItem
from scrapy.utils.project import get_project_settings

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-all']

    def parse(self, response):
        '''
        :param response: response对象
        :return: 提取分类链接
        '''
        # LinkExtractor 如不指定参数就提取页面的所有链接
        # deny 接收一个正则表达式或一个正则表达式列表，与allow相反，排除绝对url与正则表达式匹配的链接
        # 提取index.html中所有站外链接（及排除站内链接）
        le = LinkExtractor(restrict_css='div.article',
                           deny='//book.douban.com/$')
        # print(le.extract_links(response))
        for link in le.extract_links(response):
            yield scrapy.Request(
                link.url,
                callback=self.next_url_parse,
                # link.text是图书的标签，传递进行分类
                meta = {"item":link.text,
                        "url":link.url}
            )

    def next_url_parse(self,response):
        '''
        :param response:
        :return: 提取下一页链接构造请求对象
        '''
        url = response.meta["url"]
        next = '?start=%d&type=T'
        # 从settings中获取定义的变量
        setting = get_project_settings()
        for page in range(setting.get('MAX_PAGE')):
            i = page*20
            next_url = url + next %(i)
            yield scrapy.Request(
                next_url,
                callback=self.url_parse,
                meta={"item":response.meta["item"]}
            )

    # allow与deny相反，提取与正则表达式匹配的链接
    def url_parse(self,response):
        '''
        :param response: response对象
        :return: 提取详情页链接,构造请求对象
        '''
        tag = response.meta["item"]
        le = LinkExtractor(restrict_css='ul.subject-list',
                           allow='/subject/\d+/$')

        for link in le.extract_links(response):
            yield scrapy.Request(
                link.url,
                callback=self.detal_parse,
                meta={"item":tag}
            )

    def detal_parse(self,response):
        '''
        :param response: response对象
        :return: 解析详情页提取数据
        '''
        item = DoubanItem()
        infos = response.xpath('string(//div[@id="info"])').extract_first().replace('\n', '').split(":")
        for info in infos:
            if '-' in info:
                time = info[0:8]
        title = response.css('div#wrapper h1 span::text').extract_first()
        author = response.css('div#info a::text').extract_first().replace('\n','').replace(' ','')
        score = response.css('div.rating_self.clearfix strong::text').extract_first()
        # xpath的string方法提取节点下的全部文本
        content = response.css('div.indent div div.intro').xpath('string(.)')
        if content:
            content = content.extract_first().replace('\n','').replace(' ','')
        item['tag'] = response.meta["item"]
        item['book_name'] = title
        item['author'] = author
        item['time'] = time
        item['score'] = score
        item['content'] = content
        yield item






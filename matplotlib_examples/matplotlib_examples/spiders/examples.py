# -*- coding: utf-8 -*-
'''

'''
import scrapy
from scrapy.linkextractors import LinkExtractor
from matplotlib_examples.items import MatplotlibExamplesItem


class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        # LinkExtractor 如不指定参数就提取页面的所有链接
        # deny 接收一个正则表达式或一个正则表达式列表，与allow相反，排除绝对url与正则表达式匹配的链接
        # 提取index.html中所有站外链接（及排除站内链接）
        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound',
                           deny='/index.html$')

        print(len(le.extract_links(response)))
        for link in le.extract_links(response):
            # print(link.url)
            yield scrapy.Request(
                link.url,
                callback=self.parse_example
            )

    def parse_example(self,response):
        href = response.css('a.reference.external::attr(href)').extract_first()
        url = response.urljoin(href)
        item = MatplotlibExamplesItem()
        # 当FilesPipeline处理时，它会检测是否有file_urls字段，如果有的话，会将url传送给scarpy调度器和下载器
        item['file_urls'] = [url]
        yield item

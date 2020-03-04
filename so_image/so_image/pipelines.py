# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from urllib.parse import urlparse
from os.path import basename,dirname,join

# 实现一个FilesPipeline的子类，覆写file_path方法来实现所期望的文件命名规则
class MyImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        path = urlparse(request.url).path
        '''
        dirname() # 去掉文件名, 返回目录路径,
        basename() # 去掉目录路径, 返回文件名,
        join() # 将分离的各部分组合成一个路径名
        '''
        return join(basename(dirname(path)),basename(path))

class SoImagePipeline(object):
    def process_item(self, item, spider):
        return item

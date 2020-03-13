# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.project import get_project_settings
import json
from copy import deepcopy
from itjuzi.items import ItjuziItem

class ItjuziSpider(scrapy.Spider):

    name = 'IT桔子'
    allowed_domains = ['itjuzi.com']

    def start_requests(self):
        '''
        重写父类的start_requests方法，构造AJAX请求对象,dont_filter置为True防止该请求对象被过滤。
        :return: 索引页的请求对象
        '''
        settings = get_project_settings()
        cookies = {i.split("=")[0]: i.split("=")[1] for i in settings.get("COOKIES").split("; ")}
        headers = settings.get('HEADERS')
        base_url = 'https://www.itjuzi.com/api/nicorn?page=%d&com_name='
        for i in range(1,settings.get("MAX_PAGE")+1):
            index_url = base_url%(i)
            yield scrapy.Request(
                index_url,
                cookies =cookies,
                dont_filter = True
            )

    def parse(self, response):
        '''
        构造详情页的请求对象，用json解析出索引页的数据
        :param response: 索引页的响应
        :return: 详情页的请求对象
        '''
        detail_url = 'https://www.itjuzi.com/api/maxima/'
        resp_json = json.loads(response.text)
        # print(resp_json)
        item = ItjuziItem()
        data_list = resp_json.get('data').get('data')
        for data in data_list:
            item['com_id'] = data['com_id']
            item['com_name'] = data['com_name']
            item['cat_name'] = data['cat_name']
            item['sub_cat_name'] = data['sub_cat_name']
            item['com_logo_archive'] = data['com_logo_archive']
            item['com_location'] = data['com_prov']+'省'+data['com_city']+'市'
            item['invse_time'] = str(data['invse_year'])+'年'+str(data['invse_month'])+'月'+str(data['invse_day'])+'日'
            item['invse_money'] = data['invse_money']+'(%s)'%(data['round'])
            item['money'] = str(data['money'])+'/万元'


            yield scrapy.Request(
                detail_url+str(item['com_id']),
                callback = self.parse_detail,
                meta = {"item":deepcopy(item)},
            )

    def parse_detail(self,response):
        '''
        json解析出详情页需要的内容
        :param response: 详情页的响应
        :return: 需要的数据
        '''
        item = response.meta["item"]
        resp_json = json.loads(response.text)
        data = resp_json.get('data')
        item['com_born_time'] = str(data['com_born_year'])+'年'+str(data['com_born_month'])+'月'
        team_members = data['member']
        team_list=[]
        for per_list in team_members :
            team_list.append(per_list['per_name'])
            item['team_member'] =' ,'.join(team_list)
        item['com_des'] = data['com_des']
        item['com_url'] = data['com_url']

        yield item








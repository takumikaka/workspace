# -*- coding: utf-8 -*-
import scrapy


class HouseSpider(scrapy.Spider):
    name = 'house'
    allowed_domains = ['cd.lianjia.com']
    start_urls = ['http://cd.lianjia.com/']

    def parse(self, response):
        pass

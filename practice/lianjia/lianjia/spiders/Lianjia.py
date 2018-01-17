# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from lianjia.items import LianjiaItem

class LianjiaSpider(scrapy.Spider):
    name = 'Lianjia'
    allowed_domains = ['Lianjia.com']
    url = 'https://cd.lianjia.com/ershoufang/c1611047140791/?sug=%E9%94%A6%E6%B1%9F%E5%9F%8E%E5%B8%82%E8%8A%B1%E5%9B%AD%E4%B8%89%E6%9C%9F'
    start_urls = [url]

    def parse(self, response):
        bodys = Selector(response).xpath("body//div[@class='clear']")

        for body in bodys:
            item = LianjiaItem()
            item['title'] = body.xpath(
                "//div[@class='info clear']//div[@class='title']//text()").extract()
            item['total_price'] = body.xpath(
                "//div[@class='totalPrice']//span//text()").extract()
        yield item

# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from lianjia.items import LianjiaItem
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

class LianjiaSpider(CrawlSpider):
    name = 'Lianjia'
    #allowed_domains = ['Lianjia.com']
    allowed_domains = []
    #url = 'https://cd.lianjia.com/ershoufang/c1611047140791/?sug=%E9%94%A6%E6%B1%9F%E5%9F%8E%E5%B8%82%E8%8A%B1%E5%9B%AD%E4%B8%89%E6%9C%9F'
    url = 'https://cd.lianjia.com/ershoufang/chuanshi'
    start_urls = [url]

    rules=(
        Rule(LinkExtractor(allow=(r'https://cd.lianjia.com/ershoufang/chuanshi/pg\d')),callback='parse_item',follow=True),
    )

    #def parse(self, response):
    def parse_item(self, response):
        bodys = Selector(response).xpath("body//div[@class='clear']")

        for body in bodys:
            item = LianjiaItem()
            item['title'] = body.xpath(
                "//div[@class='info clear']//div[@class='title']//text()").extract()
            item['total_price'] = body.xpath(
                "//div[@class='totalPrice']//span//text()").extract()
            item['area'] = body.xpath(
                "//div[@class='houseInfo']//span[@class='houseIcon']/following::text()[2]").extract()
            item['unit_price'] = body.xpath(
                "//div[@class='priceInfo']//div[@class='unitPrice']//text()").extract()
            item['followInfo'] = body.xpath(
                "//div[@class='info clear']//div[@class='followInfo']//text()").extract()
            item['linkInfo'] = body.xpath(
                "//div[@class='info clear']//div[@class='title']//a//@href").extract()

        yield item

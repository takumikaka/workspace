# -*- coding: utf-8 -*-
import scrapy
import requests
import re
import time
from lxml import etree
from scrapy import Spider
from scrapy.selector import Selector
from lianjia.items import LianjiaItem
#from scrapy_redis.spiders import RedisSpider

class LianjiaSpider(Spider):
    name = 'Lianjia'
    allowed_domains = ['Lianjia.com']
    url = 'https://cd.lianjia.com/ershoufang/jinjiang/'
    start_urls = url

    def start_requests(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7'
        headers = {'User-Agent': user_agent}
        yield scrapy.Request(url=self.start_urls, headers=headers, method='GET', callback=self.parse)

    def parse(self, response):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7'
        headers = {'User-Agent': user_agent}
        lists = response.body.decode('utf-8')
        selector = etree.HTML(lists)
        for i in range(1, 101):
            url = 'https://cd.lianjia.com/ershoufang/jinjiang/pg{}/'.format(i)
            print('url is....', url)
            time.sleep(2)
            try:
                contents = requests.get(url)
                contents = etree.HTML(contents.content.decode('utf-8'))
                houselist = contents.xpath('/html/body/div[4]/div[1]/ul/li')
                count = 0
                for house in houselist:
                    try:
                        item = LianjiaItem()
                        item['title'] = house.xpath('div[1]/div[1]/a/text()').pop()
                        item['community'] = house.xpath('div[1]/div[2]/div/a/text()').pop()
                        item['model'] = house.xpath('div[1]/div[2]/div/text()').pop().split('|')[1]
                        item['area'] = house.xpath('div[1]/div[2]/div/text()').pop().split('|')[2]
                        item['focus_num'] = house.xpath('div[1]/div[4]/text()').pop().split('/')[0]
                        item['watch_num'] = house.xpath('div[1]/div[4]/text()').pop().split('/')[1]
                        item['time'] = house.xpath('div[1]/div[4]/text()').pop().split('/')[2]
                        item['price'] = house.xpath('div[1]/div[6]/div[1]/span/text()').pop()+'万'
                        item['link'] = house.xpath('div[1]/div[1]/a/@href').pop()
                        item['average_price'] = house.xpath('div[1]/div[6]/div[2]/span/text()').pop()
                        print("This is test.........")
                        print("count is....", count)
                        count = count + 1
                    except Exception:
                        pass
                    yield item
            except Exception:
                pass

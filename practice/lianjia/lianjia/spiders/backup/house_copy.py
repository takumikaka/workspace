from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor

from ..items import LianjiaItem

class DoubanSpider(CrawlSpider):

    name="house"

    download_delay=1

    allowed_domains=[]

    start_urls=[
        'https://cd.lianjia.com/ershoufang/jinjiang'
    ]

    rules=(
        Rule(LinkExtractor(allow=(r'https://cd.lianjia.com/ershoufang/jinjiang/pg\d')),callback='parse_item',follow=True),
    )

    def parse_item(self,response):

        print(response)

        sel=Selector(response)
        item=LianjiaItem()

        movie_name=sel.xpath('//div[@class="title"]/text()').extract()

        yield item

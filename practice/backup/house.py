from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor

from lianjia.items import LianjiaItem

class HouseSpider(CrawlSpider):

    name="house"
    download_delay=1
    allowed_domains=[]
    start_urls=[
        'https://cd.lianjia.com/ershoufang/chuanshi'
    ]
    rules=(
        Rule(LinkExtractor(allow=(r'https://cd.lianjia.com/ershoufang/chuanshi/pg\d')),callback='parse_item',follow=True),
    )

    def _fun_list(self, list, str):
        new_list = []
        for i in list:
            if i == str:
                pass
            else:
                new_list.append(i)
        return new_list

    def _pop_list(self, t_list, context):
        for i in context:
            t_list.append(i)
        return t_list


    def parse_item(self,response):
        sel=Selector(response)
        item = LianjiaItem()

        item['titles'] = sel.xpath('body//div[@class="info clear"]//div[@class="title"]//a//text()').extract()
        item['areas'] = sel.xpath("body//div[@class='houseInfo']//text()").extract()
        #item['total_prices'] = sel.xpath("body//div[@class='totalPrice']//text()").extract()
        #item['unit_prices'] = sel.xpath("body//div[@class='unitPrice']//text()").extract()
        #item['followInfos'] = sel.xpath("body//div[@class='followInfo']//text()").extract()
        #item['linkInfos'] = sel.xpath("body//div[@class='info clear']//div[@class='title']//a//@href").extract()
        return item

        '''
        titles = response.xpath('body//div[@class="info clear"]//div[@class="title"]//a//text()').extract()
        title_list = []
        self._pop_list(title_list, titles)
        print(title_list)
        item['title_list']
        areas = response.xpath("body//div[@class='houseInfo']//text()").extract()
        t_area_list = []
        self._pop_list(t_area_list, areas)
        firs_str = t_area_list[0]
        area_list = self._fun_list(t_area_list, firs_str)
        print(area_list)
        total_prices = response.xpath("body//div[@class='totalPrice']//text()").extract()
        t_total_priceList = []
        self._pop_list(t_total_priceList, total_prices)
        sec_str = t_total_priceList[1]
        total_priceList = self._fun_list(t_total_priceList, sec_str)
        print(total_priceList)
        unit_prices = response.xpath("body//div[@class='unitPrice']//text()").extract()
        unit_priceList = []
        self._pop_list(unit_priceList, unit_prices)
        print(unit_priceList)
        followInfos = response.xpath("body//div[@class='followInfo']//text()").extract()
        follow_infoList = []
        self._pop_list(follow_infoList, followInfos)
        print(follow_infoList)
        linkInfos = response.xpath("body//div[@class='info clear']//div[@class='title']//a//@href").extract()
        link_infoList = []
        self._pop_list(link_infoList, linkInfos)
        print(link_infoList)
        '''

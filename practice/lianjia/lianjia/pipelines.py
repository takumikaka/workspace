# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings

class LianjiaPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = self.client[settings['MONGODB_DB']]
        self.coll = self.db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        postItem = dict(item)
        print("Start insert MongoDB....")
        self.coll.insert(postItem)
        print("End insert MongoDB....")
        return item

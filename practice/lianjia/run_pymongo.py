# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.Spider
jinjiang = db.lianjia_jinjiang
jinjiang_area = jinjiang.find({'community': '锦江城市花园三期 ','area': {'$lt': ' 67.1平米 ', '$gt': ' 47.2平米 '}}).sort([['price', pymongo.ASCENDING]])
num = 1
for area in jinjiang_area:
    print("{0}: {1}".format(num, area))
    num += 1

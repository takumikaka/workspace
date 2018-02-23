# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient
import json
import sys

def load_file():
    try:
        with open('jinjiang.json') as json_file:
            content = json_file.read()
            data = json.load(content)
            return data
    except Exception:
        pass

def save_file(context):
    try:
        with open('jinjiang.json', 'a') as json_file:
            json_file.write('\n{0}'.format(context))
            json_file.close()
            print('Save file Successful...')
    except Exception:
        print("Save file Fail...")

client = MongoClient()
db = client.Spider
jinjiang = db.lianjia_jinjiang
jinjiang_area = jinjiang.find({'community': '锦江城市花园三期 ','area': {'$lt': ' 67.1平米 ', '$gt': ' 47.2平米 '}}).sort([['price', pymongo.ASCENDING]])
num = 1
for area in jinjiang_area:
    print("{0}: {1}".format(num, area))
    num += 1
    save_file(str(area))
    load_file()

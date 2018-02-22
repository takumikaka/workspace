# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient
import time

def get_mongodbValue():
    client = MongoClient()
    db = client.Spider
    jinjiang = db.lianjia_jinjiang
    jinjiang_dict = jinjiang.find()
    dict_count = jinjiang.find().count() + 1
    community_list = []
    print('Start community...')
    try:
        for i in range(1, dict_count):
            d_dict = jinjiang_dict[i]
            print('Get community...{0}/{1}'.format(i, dict_count))
            d = d_dict.setdefault('community', None)
            community_list.append(d)
            #time.sleep(0.5)
            #print(d)
    except Exception as e:
        pass

    time.sleep(0.5)
    print('Get community complete...')
    return community_list

def remove_dict(dict):
    list_err = ['Q城', '川附苑', '生物研究所', '晶蓝半岛一期', '天誉花园', '金红园', '锦江华庭', '绿地468公馆一期', '通用时代', '海桐三期', '翰林美居', '紫薇银座']
    for i in list_err:
        dict.pop(i)
    return dict

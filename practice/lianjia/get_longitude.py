# -*- coding: utf-8 -*-

import requests
import sys
from save_file import save_json
import time

def replace_blank(lists):
    for i in range(len(lists)):
        lists[i] = lists[i].replace(' ','')
    return lists

def get_latitude(list1, list2):
    try:
        for i in range(len(list1)):
            add = list1[i]
            print(add)
            i += 1
            print('The current progress is as follows: {0}/{1}'.format(i, len(list1)))
            time.sleep(0.5)
            print('Start get url {}...'.format(add))
            url = 'https://api.map.baidu.com/geocoder?address={}&city=成都市&output=json&key=1FPdGX4ZnhhBj4QEGyfsVBbkZM4kNWNM'.format(add)
            print('Start get latitude {}...'.format(add))
            response = requests.get(url)
            answer = response.json()
            lng = answer['result']['location']['lng']
            lat = answer['result']['location']['lat']
            count = list2[i-1]
            #local = {"add": add, "lng": lng, "lat": lat, "count": count}
            local = {"lng": lng, "lat": lat, "count": count}
            time.sleep(0.5)
            print('Start save file...')
            save_json(local)
    except Exception:
        print('Get latitude fail...')

# -*- coding: utf-8 -*-

import requests
import sys
from save_file import save_json
import time

def replace_blank(lists):
    for i in range(len(lists)):
        lists[i] = lists[i].replace(' ','')
    return lists

def get_latitude(lists):
    try:
        for i in range(len(lists)):
            add = lists[i]
            print(add)
            i += 1
            print('The current progress is as follows: {0}/{1}'.format(i, len(lists)))
            time.sleep(0.5)
            print('Start get url {}...'.format(add))
            url = 'https://api.map.baidu.com/geocoder?address={}&city=成都市&output=json&key=1FPdGX4ZnhhBj4QEGyfsVBbkZM4kNWNM'.format(add)
            print('Start get latitude {}...'.format(add))
            response = requests.get(url)
            answer = response.json()
            lng = answer['result']['location']['lng']
            lat = answer['result']['location']['lat']
            local = {'add': add, 'local': {'lng': lng, 'lat': lat}}
            time.sleep(0.5)
            print('Start save file...')
            save_json(local)
    except Exception:
        print('Get latitude fail...')

# -*- coding: utf-8 -*-
#python2.x

import urllib2
import sys
from save_file import save_json
import time
reload(sys)
sys.setdefaultencoding('utf8')

def replace_blank(lists):
    for i in range(len(lists)):
        lists[i] = lists[i].replace(' ','')
    return lists

def get_latitude(lists):
    try:
        for i in lists:
            add = i.decode('utf-8')
            time.sleep(2)
            print('Start get url {}...'.format(add))
            url = 'https://api.map.baidu.com/geocoder?address={}&city=成都市&output=json&key=1FPdGX4ZnhhBj4QEGyfsVBbkZM4kNWNM'.format(add)
            time.sleep(2)
            print('Start get latitude {}...'.format(add))
            html = urllib2.urlopen(urllib2.Request(url))
            json1 = html.read()
            time.sleep(2)
            print('Start save file...')
            save_json(json1)
    except Exception:
        print('Get latitude fail...')

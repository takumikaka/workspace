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
        for i in range(len(lists)):
            add = lists[i].decode('utf-8')
            i += 1
            print('The current progress is as follows: {0}/{1}'.format(i, len(lists)))
            time.sleep(0.5)
            print('Start get url {}...'.format(add))
            url = 'https://api.map.baidu.com/geocoder?address={}&city=成都市&output=json&key=1FPdGX4ZnhhBj4QEGyfsVBbkZM4kNWNM'.format(add)
            print('Start get latitude {}...'.format(add))
            html = urllib2.urlopen(urllib2.Request(url))
            json1 = html.read()
            time.sleep(0.5)
            print('Start save file...')
            save_json(json1)
    except Exception:
        print('Get latitude fail...')

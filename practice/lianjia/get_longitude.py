# -*- coding: utf-8 -*-
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def replace_blank(lists):
    for i in range(len(lists)):
        lists[i] = lists[i].replace(' ','')
    return lists

def get_latitude(lists):
    for i in lists:
        add = i.decode('utf-8')
        url = 'https://api.map.baidu.com/geocoder?address={}&city=成都市&output=xml&key=1FPdGX4ZnhhBj4QEGyfsVBbkZM4kNWNM'.format(add)
        html = urllib2.urlopen(urllib2.Request(url))
        xml1 = html.read()
        print(add)
        print(xml1)

# -*- coding: utf-8 -*-
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def replace_blank(lists):
    for i in range(len(lists)):
        lists[i] = lists[i].replace(' ','')
    return lists

lists = ['晶蓝半岛一期 ', '蓉上坊一期 ', '卓锦城五期 ', '卓锦城六期 ', '沙河壹号二期 ', '澳龙名城 ',
        '星河名都 ', '翡翠城四期 ', '万科金润华府 ', '锦江城市花园三期 ', '时代豪庭一期 ', '华韵天府 ',
        '翡翠城三期 ', '四海逸家二期 ', '上海东韵 ', '蓝光凯丽香江 ', '摩根中心 ', '弘邦领邸 ', '绿地锦天府 ',
        '仁恒滨河湾 ', '卓锦城一期 ', '比华利国际城一期 ', '新沙河阳光水岸 ', '比华利国际城一期 ', '卓锦城五期 ',
        '星河名都 ', '蓉上坊一期 ', '锦江城市花园二期 ', '华都美林湾 ', '卓锦城六期 '
        ]

lists = replace_blank(lists)

for i in lists:
    add = i.decode('utf-8')
    url = 'https://api.map.baidu.com/geocoder?address={}&city=成都市&output=xml&key=1FPdGX4ZnhhBj4QEGyfsVBbkZM4kNWNM'.format(add)
    html = urllib2.urlopen(urllib2.Request(url))
    xml1 = html.read()
    print(add)
    print(xml1)

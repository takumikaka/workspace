# -*- coding: utf-8 -*-

from get_longitude import replace_blank, get_latitude
from read_file import read_file
from collections import Counter
from dict_file import get_count, dict_Tolist

lists = ['龙湖晶蓝半岛一期 ', '蓉上坊一期 ', '卓锦城五期 ', '卓锦城六期 ', '沙河壹号二期 ', '澳龙名城 ',
        '星河名都 ', '翡翠城四期 ', '万科金润华府 ', '锦江城市花园三期 ', '时代豪庭一期 ', '华韵天府 ',
        '翡翠城三期 ', '四海逸家二期 ', '上海东韵 ', '蓝光凯丽香江 ', '摩根中心 ', '弘邦领邸 ', '绿地锦天府 ',
        '仁恒滨河湾 ', '卓锦城一期 ', '比华利国际城一期 ', '新沙河阳光水岸 ', '比华利国际城一期 ', '卓锦城五期 ',
        '星河名都 ', '蓉上坊一期 ', '锦江城市花园二期 ', '华都美林湾 ', '卓锦城六期 '
        ]

lists = replace_blank(lists)        # 去掉空格

list_dict = get_count(lists)        # 得到计数字典

dict_lists = list_dict.keys()       # 关键字列表
value_lists = list_dict.values()    # 键值列表

d_lists = dict_Tolist(dict_lists)   # 标准列表
v_lists = dict_Tolist(value_lists)  # 标准列表
get_latitude(d_lists, v_lists)      # 获得地址
#content = read_file("latitude.json")
#print('The json file is: {0}'.format(content))

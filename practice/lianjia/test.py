# -*- coding: utf-8 -*-


from get_longitude import replace_blank, get_latitude
from read_file import read_file
from collections import Counter
from dict_file import get_count, dict_Tolist
from get_mongodbValue import get_mongodbValue, remove_dict
from save_file import save_json

lists = get_mongodbValue()          # 取得mongodb community value

lists = replace_blank(lists)        # 去掉空格

list_dict = get_count(lists)        # 得到计数字典
list_dict = remove_dict(list_dict)
print(list_dict)

dict_lists = list_dict.keys()       # 关键字列表
value_lists = list_dict.values()    # 键值列表

d_lists = dict_Tolist(dict_lists)   # 标准列表
v_lists = dict_Tolist(value_lists)  # 标准列表

get_latitude(d_lists, v_lists)      # 获得地址
#content = read_file("latitude.json")
#print('The json file is: {0}'.format(content))
'''
d_dict = {'卓锦城六期': 15, '四海逸家二期': 35, '卓锦城五期': 18, '蓉上坊一期': 11, '沙河壹号二期': 14, '澳龙名城': 28, '星河名都': 2, '翡翠城四期': 31, '万科金润华府': 34, '锦江城市花园三期': 43}
print(d_dict)
list_err = ['四海逸家二期']
for i in list_err:
    d_dict.pop(i)
print(d_dict)
'''

# -*- coding: utf-8 -*-

def get_count(lists):
    dict = {}
    for item in lists:
        if lists.count(item) > 0:
            dict[item] = lists.count(item)
    return dict

def dict_Tolist(lists):
    dict_to_lists = []
    for i in lists:
        dict_to_lists.append(i)
    return dict_to_lists

# -*- coding:UTF-8 -*-

import json

"""
#反序列话，字典变文本
dict_data = {}
dict_data["name"] = "贝利亚"
dict_data["age"] = "未知"
dict_data["sex"] = True
dict_data["kind"] = None

print(dict_data)

with open("demo1.json", "w") as f:
    json.dump(dict_data, f)
f.close()
"""
#序列化，文本变字典

with open("demo2.json", "r") as f:
    t = f.read()
list_dict = json.loads(t)
print(list_dict["name"])

#print(dict_content["name"])
#f.close()

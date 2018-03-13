# -*- coding: utf-8 -*-


from processers.get_value import getValue
import config

########################################################################

class getDict(object):
    def __init__(self):
        self.get_value = getValue()
        self.json_2_6 = config.JSON_2_6
        self.dic_html = {}
        self.dic_json = {}

    def json_dict(self, dit, dic):
        if isinstance(dit, dict):
            for key in dit:
                if isinstance(dit[key], dict):
                    self.json_dict(dit[key], dic)
                else:
                    dic[key] = dit[key]
        else:
            print('数据不是字典类型...', dit)
        return dic

    def get_dict_html(self):
        dic = self.dic_html
        data = self.get_value.run()
        dic_html = self.json_dict(data, dic)
        return dic_html

    def get_dict_json(self):
        dic = self.dic_json
        value = self.json_2_6
        dic_json = self.json_dict(value, dic)
        return dic_json

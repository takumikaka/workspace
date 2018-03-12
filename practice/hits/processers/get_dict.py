# -*- coding: utf-8 -*-


from processers.get_value import getValue
import config

########################################################################

class getDict(object):
    def __init__(self):
        self.get_value = getValue()
        self.value = config.VALUE
        self.json_2_6 = config.JSON_2_6
        self.uid = config.UID
        self.user_info = config.USER_INFO
        self.event_info = config.EVENT_INFO
        self.os = config.OS

    def get_key(self, value, key):
        return value.get('default', {}).get(key)

    def get_userInfo(self):
        value = self.value
        return value.get(self.user_info)

    def get_eventInfo(self):
        value = self.value
        return value.get(self.event_info)

    def merg_dict(self, dict1, dict2):
        dictMerged = dict1.copy()
        dictMerged.update(dict2)
        return dictMerged

    def get_dict_html(self):
        value = self.get_value.run()

        # 家中无法连接，故读取数据调试
        dit_html = {}
        value = self.value
        dit_html[self.uid] = value.get(self.uid)
        dit_html[self.os] = value.get(self.os)
        user_info = self.get_userInfo()
        event_info = self.get_eventInfo()
        dit_html = self.merg_dict(dit_html, user_info)
        dit_html = self.merg_dict(dit_html, event_info)
        return dit_html

    def get_dict_json(self):
        dit_json = {}
        value = self.json_2_6
        dit_json[self.uid] = value.get(self.uid)
        dit_json[self.os] = value.get(self.os)
        user_info = self.get_userInfo()
        event_info = self.get_eventInfo()
        dit_json = self.merg_dict(dit_json, user_info)
        dit_json = self.merg_dict(dit_json, event_info)
        #test_dict
        dict_test = {'test':'true'}
        dit_json = self.merg_dict(dit_json, dict_test)

        return dit_json

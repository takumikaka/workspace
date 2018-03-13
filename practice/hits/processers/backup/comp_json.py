# -*- coding: utf-8 -*-

from jsondiff import diff
from processers.get_value import getValue
from processers.save_files import saveFile
import config

class compJson(object):
    def __init__(self):
        self.eid = config.EID
        self.get_value = getValue()
        self.save_file = saveFile()
        self.json_2_6 = config.JSON_2_6
        self.json_1_1 = config.JSON_1_1
        self.json_1_5 = config.JSON_1_5

    def run(self):
        get_json = self.get_value.run()
        if self.eid == '2-6':
            result = diff(self.json_2_6, get_json)
            self.save_file.save_file(str(result))
        if self.eid == '1-1':
            result = diff(self.json_1_1, get_json)
            self.save_file.save_file(str(result))
        if self.eid == '1-5':
            result = diff(self.json_1_5, get_json, )
            self.save_file.save_file(str(result))

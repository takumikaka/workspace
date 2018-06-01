# -*- coding: utf-8 -*-

from processers.read_json import readJson

class dictResources(object):

    def __init__(self):
        self.read_json = readJson()
        self.json_data_json1 = self.read_json.read_json_one()
        self.json_data_json2 = self.read_json.read_json_two()

    def get_json_resources_one(self):
        for key in self.json_data_json1:
            if key == 'resources':
                value_resources_one = self.json_data_json1['resources']
        return value_resources_one

    def get_json_resources_two(self):
        for key in self.json_data_json2:
            if key == 'resources':
                value_resources_two = self.json_data_json2['resources']
        return value_resources_two

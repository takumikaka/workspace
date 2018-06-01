# -*- coding: utf-8 -*-

from processers.dict_resources import dictResources

class checkList(object):

    def __init__(self):
        self.dict_resources = dictResources()
        self.resources_list_one = self.dict_resources.get_json_resources_one()
        self.resources_list_two = self.dict_resources.get_json_resources_two()
        self.list_one_image = []
        self.list_one_sheet = []
        self.list_two_image = []
        self.list_two_sheet = []

    def check_list_one_image(self):
        len_list = len(self.resources_list_one)
        for i in range(len_list):
            for key in self.resources_list_one[i]:
                if key == 'type' and self.resources_list_one[i]['type'] == 'image':
                    self.list_one_image.append(self.resources_list_one[i]['name'])
        return self.list_one_image

    def check_list_one_sheet(self):
        len_list = len(self.resources_list_one)
        for i in range(len_list):
            for key in self.resources_list_one[i]:
                if key == 'type' and self.resources_list_one[i]['type'] == 'sheet':
                    self.list_one_sheet += self.resources_list_one[i]['subkeys'].split(',')
        return self.list_one_sheet

    def get_list_one(self):
        list_one_image = self.check_list_one_image()
        list_one_sheet = self.check_list_one_sheet()
        list_one = list_one_image + list_one_sheet
        return list_one

    def check_list_two_image(self):
        len_list = len(self.resources_list_two)
        for i in range(len_list):
            for key in self.resources_list_two[i]:
                if key == 'type' and self.resources_list_two[i]['type'] == 'image':
                    self.list_two_image.append(self.resources_list_two[i]['name'])
        return self.list_two_image

    def check_list_two_sheet(self):
        len_list = len(self.resources_list_two)
        for i in range(len_list):
            for key in self.resources_list_two[i]:
                if key == 'type' and self.resources_list_two[i]['type'] == 'sheet':
                    self.list_two_sheet += self.resources_list_two[i]['subkeys'].split(',')
        return self.list_two_sheet

    def get_list_two(self):
        list_two_image = self.check_list_two_image()
        list_two_sheet = self.check_list_two_sheet()
        list_two = list_two_image + list_two_sheet
        return list_two

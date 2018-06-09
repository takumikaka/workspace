# -*- coding: utf-8 -*-

import json
from processers.get_cwd import getCwd

class readJson(object):
    def __init__(self):
        self.get_cwd = getCwd()
        self.part_two_cwd_json1 = 'sources/files/hghall.res.json'
        self.part_two_cwd_json2 = 'sources/files/HG_Auction.res.json'

    def read_json_one(self):
        part_one_cwd = self.get_cwd.run()
        filename = part_one_cwd + self.part_two_cwd_json1
        with open(filename) as f:
            content = f.read()
            if content.startswith(u'\ufeff'):
                content = content.encode('utf8')[3:].decode('utf8')
        data = json.loads(content)
        return data

    def read_json_two(self):
        part_one_cwd = self.get_cwd.run()
        filename = part_one_cwd + self.part_two_cwd_json2
        with open(filename) as f:
            content = f.read()
            if content.startswith(u'\ufeff'):
                content = content.encode('utf8')[3:].decode('utf8')
        data = json.loads(content)
        return data

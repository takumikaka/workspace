# -*- coding: utf-8 -*-

import json
from processers.get_cwd import getCwd

class readJson(object):
    def __init__(self):
        self.get_cwd = getCwd()
        self.part_two_cwd = 'sources/files/fengkuangdati5.8.json'

    def run(self):
        part_one_cwd = self.get_cwd.run()
        filename = part_one_cwd + self.part_two_cwd
        with open(filename) as f:
            content = f.read()
            if content.startswith(u'\ufeff'):
                content = content.encode('utf8')[3:].decode('utf8')
        data = json.loads(content)
        return data

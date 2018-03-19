# -*- coding: utf-8 -*-

import json
from processers.get_cwd import getCwd

class readJson(object):
    def __init__(self):
        self.get_cwd = getCwd()
        self.part_two_cwd = '/files/PuzzleIdiomsCfg.json'

    def run(self):
        part_one_cwd = self.get_cwd.run()
        filename = part_one_cwd + self.part_two_cwd
        with open(filename, 'r') as json_file:
            return json.load(json_file)

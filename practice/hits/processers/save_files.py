# -*- coding: utf-8 -*-

import sys
from processers.get_cwd import getCwd
import config

class saveFile(object):
    def __init__(self):
        self.get_cwd = getCwd()
        self.eid = config.EID

    def save_file(self, date):
        file_name = self.get_cwd.run() + '/files/eid' + self.eid + '.txt'
        f = open(file_name,'a')
        f.write(date + '\n')
        f.close()

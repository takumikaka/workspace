# -*- coding: utf-8 -*-

from processers.get_cwd import getCwd
from processers.open_xls import openXls
import os

class songDown():
    def __init__(self):
        self.get_cwd = getCwd()
        self.open_xls = openXls()

    def run(self):
        lst = self.open_xls.run()
        len_lst = len(lst)
        for i in range(len_lst):
            song_url = lst[i]
            song_name = lst[i].split('/')[5]
            filePath = 'sources/mp3/{0}'.format(song_name)
            c = "wget \"%s\" -c -T 10 -t 10 -O \"%s\"" % (song_url, filePath)
            os.system(c.encode('utf-8'))

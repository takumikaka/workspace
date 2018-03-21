# -*- coding: utf-8 -*-

from processers.get_cwd import getCwd
import base64
import urllib.parse

class openFile(object):
    def __init__(self):
        self.get_cwd = getCwd()
        self.pwd_part_two = 'pics/crop_test1.png'

    def get_filename(self):
        pwd_part_one = self.get_cwd.run()
        filename = pwd_part_one + self.pwd_part_two
        return filename

    def get_base64(self):
        filename = self.get_filename()
        f = open(filename, 'rb')
        img = base64.b64encode(f.read())
        return img

    def get_params(self):
        img = self.get_base64()
        params = {'image': img}
        params = urllib.parse.urlencode(params)
        return params

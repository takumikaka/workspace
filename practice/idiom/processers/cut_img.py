# -*- coding: utf-8 -*-

from processers.get_cwd import getCwd
from PIL import Image
import os

class cutImg(object):
    def __init__(self):
        self.get_cwd = getCwd()
        self.pwd_part_two = 'pics/test2.jpg'

    def get_filename(self):
        pwd_part_one = self.get_cwd.run()
        filename = pwd_part_one + self.pwd_part_two
        return filename

    def run(self):
        filename = self.get_filename()
        im = Image.open(filename)
        img_size = im.size
        print("图片宽度和高度分别是{}".format(img_size))
        x = 50
        y = 200
        w = 450
        h = 420
        region = im.crop((x, y, x+w, y+h))
        region.save(self.get_cwd.run() + "pics/crop_test1.jpg")

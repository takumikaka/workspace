# -*- coding: utf-8 -*-

import urllib.request
from processer.open_xls import openXls
from processer.get_cwd import getCwd

################################################################################

class saveImg(object):
    def __init__(self):
        self.open_xls = openXls()
        self.get_cwd = getCwd()
        self.part_pwd_two = self.part_pwd_two = 'resource/images/'
        self.st_a = 'a'
        self.num_a = 2
        self.st_b = 'b'
        self.num_b = 3

    def save_img(self, lst, pwd, st, num):
        for i in range(len(lst)):
            url = lst[i][num]
            urllib.request.urlretrieve(url, pwd+'{0}{1}.jpg'.format(st, i+1))
            print('save...{0}{1}.jpg...completely...'.format(st, i+1))
            i += 1

    def run(self):
        part_pwd_one = self.get_cwd.run()
        pwd = part_pwd_one + self.part_pwd_two
        lst = self.open_xls.run()
        save_img_a = self.save_img(lst, pwd, self.st_a, self.num_a)
        save_img_b = self.save_img(lst, pwd, self.st_b, self.num_b)


################################################################################

def main():
    action = saveImg()
    action.run()

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

import sys
import json

def save_file(content):
    try:
        with open('jinjiang.json', 'a') as json_file:
            json_file.write('\n{0}'.format(content))
            json_file.close()
            print('Save file Successful...')
    except Exception:
        print('Save file Fail.....')

for i in range(1, 10):
    save_file(str(i))
    print(i)

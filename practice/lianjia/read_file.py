# -*- coding: utf-8 -*-

import sys
import time

def read_file(filename):
    try:
        time.sleep(2)
        print('Start read file...')
        with open(filename) as f:
            content = f.read()
        time.sleep(2)
        print('Read complete...')
        return content
    except Exception:
        time.sleep(2)
        print('Read file fail...')

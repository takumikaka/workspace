# -*- coding: utf-8 -*-

import sys
import time

def read_file(filename):
    try:
        time.sleep(0.5)
        print('Start read file...')
        with open(filename) as f:
            content = f.read()
        print('Read complete...')
        return content
    except Exception:
        time.sleep(0.5)
        print('Read file fail...')

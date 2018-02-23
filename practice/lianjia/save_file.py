# -*- coding: utf-8 -*-
import time

def save_json(context):
    try:
        with open('latitude.json', 'a') as json_file:
            json_file.write('\n{0}'.format(context))
            json_file.close()
            time.sleep(0.5)
            print('Save file Successful...')
    except Exception:
        print("Save file Fail...")

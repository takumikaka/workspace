# -*- coding: utf-8 -*-

def save_json(context):
    try:
        with open('latitude.json', 'a') as json_file:
            print('Satrt save file...')
            json_file.write('\n{0}'.format(context))
            json_file.close()
            print('Save file Successful...')
    except Exception:
        print("Save file Fail...")

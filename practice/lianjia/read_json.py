# -*- coding: utf-8 -*-

import json

def load():
    with open('items.json') as json_file:
        return json.load(json_file)

if __name__ == "__main__":

    data = load()
    print(data)

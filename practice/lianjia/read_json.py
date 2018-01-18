# -*- coding: utf-8 -*-

import json

def load():
    filename = input("Enter the json file name:")
    with open(filename) as json_file:
        return json.load(json_file)

if __name__ == "__main__":

    data = load()
    print(data)

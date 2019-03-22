# coding:UTF-8 -*-

import sys
import json
sys.path.append("..")
from lib.read_excel import *

def get_city_id(city_name):
    data = get_list_data(city_name)
    city_id = data["City_ID"]
    return city_id

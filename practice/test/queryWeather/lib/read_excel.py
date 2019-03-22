# coding:UTF-8 -*-

import xlrd
import sys
sys.path.append("..")
from config.config import *

def excel_to_list():
    data_list = []
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name("china-city-list")
    header = sh.row_values(2)
    for i in range(3, sh.nrows):
        d = dict(zip(header, sh.row_values(i)))
        data_list.append(d)
    return data_list

def get_list_data(city_name):
    data_list = excel_to_list()
    try:
        for data in data_list:
            if city_name == data["City_CN"]:
                return data
    except Exception as e:
        logging.error(str(e))

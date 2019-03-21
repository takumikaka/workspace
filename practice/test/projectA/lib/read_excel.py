# coding:UTF-8 -*-

import xlrd
import sys
sys.path.append("..")
from config.config import *

def excel_to_list(sheet_name):
    data_list = []
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet_name)
    header = sh.row_values(1)
    for i in range(2, sh.nrows):
        data = dict(zip(header, sh.row_values(i)))
        data_list.append(data)
    return data_list

def get_data_case(sheet_name, case_name):
    data_list = excel_to_list(sheet_name)
    for data_case in data_list:
        if case_name == data_case["case name"]:
            return data_case

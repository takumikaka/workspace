# coding:UTF-8 -*-

import xlrd
from config import *

def excel_to_list():
    data_list = []
    wb = xlrd.open_workbook(data_path)
    sh = wb.sheet_by_name(sheet_name)
    headers = sh.row_values(1)
    for i in range(2, sh.nrows):
        data = dict(zip(headers, sh.row_values(i)))
        if len(data) >= 2:
            data_list.append(data[0])
    return data_list

def get_test_data(case_name):
    for case_data in excel_to_list():
        if case_name == case_data["case name"]:
            return case_data

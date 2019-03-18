# coding:UTF-8 -*-

import xlrd

def excel_to_list(file_name, sheet_name):
    data_list = []
    wb = xlrd.open_workbook(file_name)
    sh = wb.sheet_by_name(sheet_name)
    header = sh.row_values(1)
    for i in range(2, sh.nrows):
        data = dict(zip(header, sh.row_values(i)))
        data_list.append(data)
    return data_list

def get_test_data(data_list, case_name):
    for case_data in data_list:
        if case_name == case_data["case name"]:
            return case_data

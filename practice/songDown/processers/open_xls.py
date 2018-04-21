# -*- coding: utf-8 -*-


import xlrd
from processers.get_cwd import getCwd
#from get_cwd import getCwd

############################################################################

class openXls(object):

    def __init__(self):
        self.get_cwd = getCwd()
        self.part_pwd_two = 'sources/files/mp30420.xlsx'
        self.sheet_index = 0

    def get_lst(self, sheet):

        data = []
        for i in range(0, sheet.ncols):
            data.append(sheet.col_values(i))
        return data

    def run(self):
        part_pwd_one = self.get_cwd.run()
        pwd = part_pwd_one + self.part_pwd_two
        workbook = xlrd.open_workbook(u'{0}'.format(pwd))
        sheet = workbook.sheet_by_index(self.sheet_index)
        data = self.get_lst(sheet)
        data.remove(data[-1])
        data = data[0]
        return data


############################################################################

def main():
    action = openXls()
    action.run()

if __name__ == '__main__':
    main()

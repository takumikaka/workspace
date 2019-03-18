# coding:UTF-8 -*-

import xlrd

wb = xlrd.open_workbook("test_user_data.xlsx")
sh = wb.sheet_by_name("TestUserLogin")
#print(sh.nrows)
#print(sh.ncols)
#print(sh.cell(1, 0).value)
#print(sh.row_values(1))
#print(sh.row_values(2))

print(dict(zip(sh.row_values(1), sh.row_values(2))))
print(dict(zip(sh.row_values(1), sh.row_values(3))))

#for i in range(1, sh.nrows):
#    print(sh.row_values(i))

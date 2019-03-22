# coding:UTF-8 -*-

from db2 import DB

db = DB()
if db.check_user("xiang"):
    db.delete_user("xiang")
result = db.check_all()
print(result)

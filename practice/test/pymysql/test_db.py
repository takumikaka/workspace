# coding:UTF-8 -*-

from db import DB

db = DB()

db.add_user("xiao")
result = db.check_all()
print(result)
if db.check_user("xiao"):
    db.delete_user("xiao")
result = db.check_all()
print(result)

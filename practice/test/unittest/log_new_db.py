# coding:UTF-8 -*-

from new_db import NewDB

new_db = NewDB()

class TestNewDb(object):
    def __init__(self):
        pass

    def run(self):
        sql = new_db.check_user("张三")
        new_db.query(sql)

def main():
    Action = TestNewDb()
    Action.run()

if __name__ == "__main__":
    main()

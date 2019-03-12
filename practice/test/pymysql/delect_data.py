# coding:UTF-8 -*-

import pymysql

class DelectData(object):
    def __init__(self):
        pass

    def db_connect(self):
        db = pymysql.connect("localhost", "root", "raspberry", "pymysql_test")
        cursor = db.cursor()
        return db, cursor

    def sql_str(self):
        sql_str = "DELETE FROM EMPLOYEE WHERE INCOME > %d" % (9999)
        return sql_str

    def delect_data(self, db, cursor, sql_str):
        try:
            cursor.execute(sql_str)
            db.commit()
        except:
            print("数据不合法!")
        db.close()

    def run(self):
        db, cursor = self.db_connect()
        sql_str = self.sql_str()
        self.delect_data(db, cursor, sql_str)

def main():
    Action = DelectData()
    Action.run()

if __name__ == "__main__":
    main()

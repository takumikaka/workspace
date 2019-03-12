# coding:UTF-8 -*-

import pymysql

class UpdateData(object):
    def __init__(self):
        pass

    def db_connect(self):
        db = pymysql.connect("localhost", "root", "raspberry", "pymysql_test")
        cursor = db.cursor()
        return db, cursor

    def sql_str(self):
        sql_str = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%s'" % ('M')
        return sql_str

    def update_data(self, db, cursor, sql_str):
        try:
            cursor.execute(sql_str)
            db.commit()
        except:
            db.rollback()
        db.close()

    def run(self):
        db, cursor = self.db_connect()
        sql_str = self.sql_str()
        self.update_data(db, cursor, sql_str)

def main():
    Action = UpdateData()
    Action.run()

if __name__ == "__main__":
    main()

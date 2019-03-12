# coding:UTF-8 -*-

import pymysql

class InsertData(object):
    def __init__(self):
        pass

    def db_connect(self):
        db = pymysql.connect("localhost", "root", "raspberry", "pymysql_test")
        cursor = db.cursor()
        return db, cursor

    def sql_str(self):
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
                LAST_NAME, AGE, SEX, INCOME)
                VALUES ('Bruce', 'Wayne', 45, 'M', 2016)"""
        return sql

    def insert_sql(self, db, cursor, sql_str):
        try:
            cursor.execute(sql_str)
            db.commit()
        except:
            db.rollback()
        db.close()

    def run(self):
        db, cursor = self.db_connect()
        sql = self.sql_str()
        self.insert_sql(db, cursor, sql)

def main():
    Action = InsertData()
    Action.run()

if __name__ == "__main__":
    main()

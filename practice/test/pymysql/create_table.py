# coding: UTF-8 -*-

import pymysql

class CreateTable(object):
    def __init__(self):
        pass

    def db_connect(self):
        db = pymysql.connect("localhost", "root", "raspberry", "pymysql_test")
        cursor = db.cursor()
        return db, cursor

    def insert_sql(self):
        sql_str = """CREATE TABLE EMPLOYEE(
                FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT)"""
        return sql_str

    def create_table(self, db, cursor, sql_str):
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE;")
        cursor.execute(sql_str)
        cursor.execute("SHOW TABLES;")
        db.close()

    def run(self):
        db, cursor = self.db_connect()
        sql_str = self.insert_sql()
        self.create_table(db, cursor, sql_str)

def main():
    Action = CreateTable()
    Action.run()

if __name__ == "__main__":
    main()

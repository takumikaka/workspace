# coding:UTF-8 -*-

import pymysql

class DB(object):
    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "raspberry", "pymysql_test")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

    def check_user(self, str):
        result = self.query("select * from employee where first_name = '{0}';".format(str))
        return True if result else False

    def delete_user(self, str):
        self.exec("delete from employee where first_name = '{0}';".format(str))

    def check_all(self):
        result = self.query("select * from employee;")
        return result

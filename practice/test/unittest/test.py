# coding:UTF-8 -*-

import pymysql

class Test(object):
    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "raspberry", "unittest_db")
        self.cur = self.conn.cursor()

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def check_user(self, name):
        sql = "select * from user where name = '{0}'".format(name)
        result = self.query(sql)
        return True if result else False

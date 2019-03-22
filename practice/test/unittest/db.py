# coding:UTF-8 -*-

import pymysql

class DB(object):
    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "raspberry", "unittest_db")
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        self.cur.close()

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

    def check_user(self, name):
        result = self.query("select * from user where name = '{0}';".format(name))
        return True if result else False

    def add_user(self, name, password):
        self.exec("insert into user(name, password) values('{0}', '{1}');".format(name, password))

    def del_user(self, name):
        self.exec("delete from user where name = '{0}'".format(name))

# coding:UTF-8 -*-

import pymysql
from config import *

class NewDB(object):
    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "raspberry", "unittest_db")
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        logging.info(sql)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        logging.info(result)
        return result

    def exec(self, sql):
        logging.info(sql)
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logging.info(str(e))

    def check_user(self, user_name):
        sql = "select * from user where name = '{0}';".format(user_name)
        return sql

    def add_user(self, user_name, password):
        sql = "insert into user(name, password) values('{0}', '{1}');".format(user_name, password)
        return sql

    def del_user(self, user_name):
        sql = "delete from user where name = '{0}';".format(user_name)
        return sql

# coding:UTF-8 -*-

import pymysql
import sys
sys.path.append("..")
from config.config import *

class DB(object):
    def __init__(self):
        self.conn = pymysql.connect(db_host, db_user, db_passwd, db)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logging.error(str(e))

    def check_user(self, name):
        result = self.query("select * from user where name = '{0}';".format(name))
        return True if result else False

    def add_user(self, name, passwd):
        self.exec("insert into user(name, password) values('{0}', '{1}');".format(name, passwd))

    def del_user(self, name):
        self.exec("delete from user where name = '{0}';".format(name))

# coding:UTF-8 -*-

############################################
# 获取链接方法
# 封装数据库查询
# 封装更改数据库操作
# 封装常用数据库
############################################

import pymysql

class DB(object):
    def __init__(self):
        self.conn = pymysql.connect(
                "localhost",
                "root",
                "raspberry",
                "pymysql_test"
        )
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        try:
            self.cur.execute(sql)
            result = self.cur.fetchall()
        except Exception as e:
            print(e)
        finally:
            return result

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

    def check_user(self, str):
        sql = "select * from employee where first_name = '{0}';".format(str)
        result = self.query(sql)
        return True if result else False

    def check_all(self):
        sql = "select * from employee;"
        result = self.query(sql)
        return result

    def add_user(self, str):
        sql = "insert into employee(first_name) values ('{0}');".format(str)
        self.exec(sql)

    def delete_user(self, str):
        sql = "delete from employee where first_name = '{0}';".format(str)
        self.exec(sql)

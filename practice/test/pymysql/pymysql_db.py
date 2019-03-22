# coding:UTF-8 -*-

############################################
# 获取链接方法
# 封装数据库查询
# 封装更改数据库操作
# 封装常用数据库
############################################

import pymysql

class PymysqlDB(object):
    def __init__(self):
        pass

    def input_firstName(self):
        first_name = input("Input first_name: ")
        return first_name

    def input_lastName(self):
        last_name = input("Input last_name: ")
        return last_name

    def connect_db(self):
        db = pymysql.connect(
                "localhost",
                "root",
                "raspberry",
                "pymysql_test"
        )
        return db

    def query_db(self, mysql_str):
        db = self.connect_db()
        cursor = db.cursor()
        try:
            cursor.execute(mysql_str)
            result = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            db.close()
            return result

    def change_db(self, mysql_str):
        db = self.connect_db()
        cursor = db.cursor()
        try:
            cursor.execute(mysql_str)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
        finally:
            cursor.close()
            db.close()

    def check_all(self):
        mysql_str = "select * from employee;"
        results = self.query_db(mysql_str)
        print(results)
        return True if results else False

    def check_user(self):
        first_name = self.input_firstName()
        last_name = self.input_lastName()
        mysql_str = "select * from employee where first_name = '{0}' and last_name = '{1}';".format(first_name, last_name)
        result = self.query_db(mysql_str)
        return True if result else False

    def add_user(self):
        first_name = self.input_firstName()
        last_name = self.input_lastName()
        mysql_str = "insert into employee(first_name, last_name) values ('{0}', '{1}');".format(first_name, last_name)
        self.change_db(mysql_str)

    def delete_user(self):
        first_name = self.input_firstName()
        last_name = self.input_lastName()
        mysql_str = "delete from employee where first_name = '{0}' and last_name = '{1}';".format(first_name, last_name)
        self.change_db(mysql_str)

    def run(self):
        print("query all table datas: ")
        self.check_all()
        print("query one table datas: ")
        self.check_user()
        print("add one table data: ")
        self.add_user()
        print("delete one table data: ")
        self.delete_user()
        print("query new table datas: ")
        self.check_all()

def main():
    Action = PymysqlDB()
    Action.run()

if __name__ == "__main__":
    main()

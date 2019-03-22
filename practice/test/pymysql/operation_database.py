# coding:UTF-8 -*-

import pymysql

class OperationDatabase(object):
    def __init__(self):
        pass

    def db_connect(self):
        db = pymysql.connect("localhost", "root", "raspberry", "pymysql_test", charset = "utf8")
        cursor = db.cursor()
        return db, cursor

    def add_table(self, db, cursor):
        mysql_str1 = "insert into employee(first_name, last_name, age, sex, income) values ('张', '三', 19, 'M', 1998);"
        mysql_str2 = "insert into employee(first_name, last_name, age, sex, income) values ('筱', '蕊', 23, 'F', 2003);"
        try:
            cursor.execute(mysql_str1)
            cursor.execute(mysql_str2)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)

    def check_onedata(self, cursor):
        cursor.execute("select * from employee where first_name = '张';")
        result_onedata = cursor.fetchall()
        return result_onedata

    def delete_data(self, db, cursor):
        try:
            cursor.execute("delete from employee where age = %d;" % (23))
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)

    def check_data(self, cursor):
        cursor.execute("select * from employee;")
        results = cursor.fetchall()
        return results

    def run(self):
        db, cursor = self.db_connect()
        self.add_table(db, cursor)
        result_onedata = self.check_onedata(cursor)
        print(result_onedata)
        self.delete_data(db, cursor)
        results = self.check_data(cursor)
        print(results)
        db.close()

def main():
    Action = OperationDatabase()
    Action.run()

if __name__ == "__main__":
    main()

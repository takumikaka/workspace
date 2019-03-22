# coding:UTF-8 -*-

import pymysql

class CheckData(object):
    def __init__(self):
        pass

    def db_connect(self):
        db = pymysql.connect("localhost", "root", "raspberry", "pymysql_test")
        cursor = db.cursor()
        return db, cursor

    def sql_str(self):
        sql_str = "SELECT * FROM EMPLOYEE \
                    WHERE INCOME > %s;" % (2000)
        return sql_str

    def check_data(self, db, cursor, sql_str):
        try:
            cursor.execute(sql_str)
            results = cursor.fetchall()
        except Exception as e:
            db.rollback()
            print(e)
        return results

    def dict_list(self, dict_list):
        try:
            for row in dict_list:
                fName = row[0]
                lName = row[1]
                age = row[2]
                sex = row[3]
                income = row[4]
            print("Welcome {0} {1}, he's age {2}.".format(fName, lName, age))
        except Exception as e:
            print(e)

    def run(self):
        db, cursor = self.db_connect()
        sql_str = self.sql_str()
        results = self.check_data(db, cursor, sql_str)
        self.dict_list(results)
        db.close()

def main():
    Action = CheckData()
    Action.run()

if __name__ == "__main__":
    main()

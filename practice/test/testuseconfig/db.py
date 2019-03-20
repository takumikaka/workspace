# coding:UTF-8 -*-

import pymysql
from config import *

def conn_db():
    conn = pymysql.connect(db_host, db_user, db_passwd, db)

def cur_db():
    cur = conn_db().cursor()

def close_db():
    conn_db().close()

def close_cur():
    cur_db().close()

def query(sql):
    cur_db().execute(sql)
    result = cur_db().fetchall()
    close_cur()
    close_db()
    return result

def exec(sql):
    try:
        cur_db().execute(sql)
        conn_db().commit()
    except Exception as e:
        conn_db().rollback()
        logging.error(str(e))
    finally:
        close_cur()
        close_db()

def check_user(name):
    result = query("select * from user where name = '{0}';".format(name))
    return True if result else False

def add_user(name, passwd):
    exec("insert into user(name, password) values('{0}', '{1}');".format(name, passwd))

def del_user(name):
    exec("delete from user where name = '{0}';".format(name))

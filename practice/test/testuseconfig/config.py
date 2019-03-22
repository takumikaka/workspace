# coding:UTF-8 -*-

import os
import logging

path_prj = os.path.dirname(os.path.abspath(__file__))

data_path = os.path.join(path_prj, "test_user_data.xlsx")
sheet_name = "TestUserLogin"
case_name_one = "test_user_login_normal"
case_name_two = "test_user_login_wrong"

log_file = os.path.join(path_prj, "log.txt")
report_file = os.path.join(path_prj, "report.html")

logging.basicConfig(level = logging.DEBUG,
                    format = "[%(asctime)s]  %(levelname)s [%(funcName)s: %(filename)s %(lineno)s] %(message)s",
                    datefmt = "%Y-%m-%d %H-%M-%S",
                    filename = log_file,
                    filemode = "a")

db_host = "localhost"
db_user = "root"
db_passwd = "raspberry"
db = "unittest_db"

smtp_server = "smtp.163.com"
smtp_user = ""
smtp_passwd = ""

sender = "{0}@163.com".format(smtp_user)
receiver = "@qq.com"
subject = "接口测试报告"

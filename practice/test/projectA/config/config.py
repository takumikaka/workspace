# coding:UTF-8 -*-

import logging
import os

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_file = os.path.join(prj_path, "data", "test_user_data.xlsx")
test_path = os.path.join(prj_path, "test")

sheet_name_login = "TestUserLogin"
sheet_name_reg = "TestUserReg"
case_name_lognor = "test_user_login_normal"
case_name_logwro = "test_user_login_wrong"
case_name_regnor = "test_user_reg_nomal"
case_name_regist = "test_user_reg_exist"
passwd = "123456"

log_file = os.path.join(prj_path, "log", "log.txt")
report_file = os.path.join(prj_path, "report", "report.html")

logging.basicConfig(level=logging.DEBUG,
                    format="[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s %(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H: %M: %S",
                    filename=log_file,
                    filemode="a")

db_host = "localhost"
db_user = "root"
db_passwd = "raspberry"
db = "unittest_db"

smtp_server =  "smtp.163.com"
smtp_user = ""
smtp_passwd = ""

sender = "{0}@163.com".format(smtp_user)
receiver = "@qq.com"
subject = "接口测试报告"

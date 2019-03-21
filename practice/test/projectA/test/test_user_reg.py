# coding:UTF-8 -*-

import unittest
import requests
import json
import sys
import re
sys.path.append("..")
from lib.case_log import *
from lib.read_excel import *
from config.config import *
from lib.db import *

PASSWD = "123456"

db = DB()

class TestUserReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_case_regnor = get_data_case(sheet_name_reg, case_name_regnor)
        cls.data_case_regist = get_data_case(sheet_name_reg, case_name_regist)

    def get_name_usernor(self):
        data = self.data_case_regnor["data"]
        dict_data = json.loads(data)
        return dict_data["name"]

    def get_name_userist(self):
        data = self.data_case_regist["data"]
        dict_data = json.loads(data)
        return dict_data["name"]


    def test_user_reg_normal(self):
        if db.check_user(self.get_name_usernor()):
            db.del_user(self.get_name_usernor())

        if not self.data_case_regnor:
            logging.info("数据不存在!")

        url = self.data_case_regnor["url"]
        data = self.data_case_regnor["data"]
        expect_data = self.data_case_regnor["expect_data"]
        res = requests.post(url = url, json = json.loads(data))
        res_data = re.sub('\'', '\"', str(res.json()))

        log_case_info(case_name_regnor, url, data, expect_data, json.loads(res_data))
        self.assertEqual(json.loads(res_data), json.loads(expect_data))

        db.add_user(self.get_name_usernor(), PASSWD)
        self.assertTrue(db.check_user(self.get_name_usernor()))
        db.del_user(self.get_name_usernor())

    def test_user_reg_exist(self):
        if not db.check_user(self.get_name_userist()):
            db.add_user(self.get_name_userist(), PASSWD)

        if not self.data_case_regist:
            logging.info("数据不存在!")

        url = self.data_case_regist["url"]
        data = self.data_case_regist["data"]
        expect_data = self.data_case_regist["expect_data"]
        res = requests.post(url = url, json = json.loads(data))
        res_data = res.text

        log_case_info(case_name_regist, url, data, expect_data, res_data)
        self.assertEqual(json.loads(res_data), json.loads(expect_data))

if __name__ == "__main__":
    unittest.main(verbosity=2)

# coding:UTF-8 -*-

import unittest
import json
import requests
import sys
sys.path.append("..")
from config.config import *
from lib.case_log import *
from lib.db import *
from lib.read_excel import *

db = DB()

class TestUserReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_user_regnor = get_data_case(sheet_name_reg, case_name_regnor)
        cls.data_user_regwro = get_data_case(sheet_name_reg, case_name_regist)

    def get_regnor_name(self):
        data = self.data_user_regnor["data"]
        dict_data = json.loads(data)
        return dict_data["name"]

    def get_regwro_name(self):
        data = self.data_user_regwro["data"]
        dict_data = json.loads(data)
        return dict_data["name"]

    def test_user_regnor(self):
        if db.check_user(self.get_regnor_name()):
            del_user(self.get_regnor_name())

        url = self.data_user_regnor["url"]
        data = self.data_user_regnor["data"]
        expect_data = self.data_user_regnor["expect_data"]
        res = requests.post(url=url, json=json.loads(data))
        res_data = json.loads(res.text)
        log_case_info(case_name_regnor, url, data, expect_data, res_data)

        self.assertEqual(res_data, json.loads(expect_data))

        db.add_user(self.get_regnor_name(), passwd)
        self.assertTrue(db.check_user(self.get_regnor_name()))
        db.del_user(self.get_regnor_name())

    def test_user_regwro(self):
        if not db.check_user(self.get_regwro_name()):
            add_user(self.get_regwro_name())

        url = self.data_user_regwro["url"]
        data = self.data_user_regwro["data"]
        expect_data = self.data_user_regwro["expect_data"]
        res = requests.post(url=url, json=json.loads(data))
        res_data = json.loads(res.text)
        log_case_info(case_name_regist, url, data, expect_data, res_data)

        self.assertEqual(res_data, json.loads(expect_data))

if __name__ == "__main__":
    unittest.main(verbosity=2)

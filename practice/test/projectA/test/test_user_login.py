# coding:UTF-8 -*-

import unittest
import requests
import json
import sys
sys.path.append("..")
from config.config import *
from lib.case_log import *
from lib.db import *
from lib.read_excel import *

class TestUserReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_user_lognor = get_data_case(sheet_name_login, case_name_lognor)
        cls.data_user_logwro = get_data_case(sheet_name_login, case_name_logwro)

    def test_user_login_nomal(self):
        if not self.data_user_lognor:
            logging.info("数据不存在!")
        else:
            url = self.data_user_lognor["url"]
            data = self.data_user_lognor["data"]
            expect_data = self.data_user_lognor["expect_data"]

            res = requests.post(url=url, data=json.loads(data))
            res_data = res.text
            log_case_info(case_name_lognor, url, data, expect_data, res_data)

            self.assertEqual(res_data, expect_data)

    def test_user_login_wrong(self):
        if not self.data_user_logwro:
            logging.info("数据不存在!")
        else:
            url = self.data_user_logwro["url"]
            data = self.data_user_logwro["data"]
            expect_data = self.data_user_logwro["expect_data"]

            res = requests.post(url=url, data=json.loads(data))
            res_data = res.text
            log_case_info(case_name_logwro, url, data, expect_data, res_data)

            self.assertEqual(res_data, expect_data)

if __name__ == "__main__":
    unittest.main(verbosity=2)

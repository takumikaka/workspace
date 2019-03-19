# coding:UTF-8 -*-

import unittest
import json
import requests
from read_excel import *
from case_log import *

class LogCaseLog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list("test_user_data.xlsx", "TestUserLogin")

    def test_log_case_log(self):
        case_name = "test_user_login_normal"
        case_data = get_test_data(self.data_list, case_name)

        if not case_data:
            logging.info("数据不存在!")

        url = case_data["url"]
        data = case_data["data"]
        expect_data = case_data["expect_data"]
        res = requests.post(url = url, data = json.loads(data))
        res_data = res.text
        log_case_info(case_name, url, data, expect_data, res_data)

        self.assertEqual(res_data, expect_data)

if __name__ == "__main__":
    unittest.main(verbosity=2)

# coding:UTF-8 -*-

import unittest
import requests
import json
from read_excel import *

class InterTestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list("test_user_data.xlsx", "TestUserLogin")

    def test_user_login_normal(self):
        data_case = get_test_data(self.data_list, "test_user_login_normal")

        if not data_case:
            print("数据不存在!")

        url = data_case["url"]
        data = data_case["data"]
        expect_data = data_case["expect_data"]

        res = requests.post(url = url, data = json.loads(data))
        res_data = res.text

        self.assertEqual(res.text, expect_data)

if __name__ == "__main__":
    unittest.main(verbosity=2)

# coding:UTF-8 -*-

import unittest
import requests
from HTMLTestReportCN import HTMLTestRunner

class TestUserLogin(unittest.TestCase):

    url = "http://115.28.108.130:5000/api/user/login/"

    def test_user_login_normal(self):
        data = {"name": "张三", "password": "123456"}
        res = requests.post(url=self.url, data=data)
        self.assertIn("成功", res.text)

    def test_user_login_wrong(self):
        data = {"name": "张三", "password": "1234567"}
        res = requests.post(url=self.url, data=data)
        self.assertIn("失败", res.text)

if __name__ == "__main__":
    unittest.main(verbosity=2)
    #test_suite = unittest.TestSuite()
    #test_suite.addTest(unittest.makeSuite(TestUserLogin))
    #with open("test_user_login.html", "wb") as f:
    #    runner = HTMLTestRunner(stream=f, title=None, description=None)
    #    runner.run(test_suite)

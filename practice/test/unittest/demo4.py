# coding:UTF-8 -*-

from HTMLTestReportCN import HTMLTestRunner
import unittest
import requests

class Mytest(unittest.TestCase):

    def get_content(self):
        url = "http://115.28.108.130:5000/api/user/login/"
        data = {"name": "张三", "password": "123456"}
        html = requests.post(url = url, data = data)
        content = html.text
        return content

    def test_login_success(self):
        content = self.get_content()
        self.assertEqual(content, "<h1>登录成功</h1>")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Mytest)
    unittest.TextTestRunner(verbosity=2).run(suite)

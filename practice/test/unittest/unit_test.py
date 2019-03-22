# coding:UTF-8 -*-

import unittest
from test import Test

test = Test()

class MyTest(unittest.TestCase):

    def test_IsTrue(self):
        self.assertTrue(test.check_user("项少龙"))

    def test_isEqual(self):
        data1 = {'code': '100001', 'data': {'name': '张三', 'password': 'e10adc3949ba59abbe56e057f20f883e'}, 'msg': '失败，用户已存在'}
        data2 = {"code":"100001","data":{"name":"张三","password":"e10adc3949ba59abbe56e057f20f883e"},"msg":"失败，用户已存在"}

        self.assertEqual(data1, data2)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    test_suite = unittest.TestSuite()
    test_suite.addTest(MyTest("test_isEqual"))
    unittest.TextTestRunner(verbosity=2).run(test_suite)

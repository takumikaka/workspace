# coding:UTF-8 -*-

import unittest

class Mytest(unittest.TestCase):
    def tearDown(self):
        print("每个测试用例执行完成后执行卸载操作")

    def setUp(self):
        print("每个测试用例执行之前执行安装操作")

    @classmethod
    def tearDownClass(self):
        print("每个程序执行完毕后执行该操作")

    @classmethod
    def setUpClass(self):
        print("每个程序执行前先执行该操作")

    def test_run_a(self):
        self.assertEqual(1, 1)

    def test_run_b(self):
        self.assertEqual(2, 2)

if __name__ == "__main__":
    unittest.main()

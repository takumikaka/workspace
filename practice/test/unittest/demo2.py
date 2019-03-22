# coding:UTF-8 -*-

from HTMLTestReportCN import HTMLTestRunner
import unittest

class MyTest(unittest.TestCase):
    def tearDown(self):
        print("用例执行完成后，执行该语句")

    def setUp(self):
        print("用例执行开始前，执行该语句")

    @classmethod
    def tearDownClass(self):
        print("程序执行完成后，执行该语句")

    @classmethod
    def setUpClass(self):
        print("程序执行开始前，执行该语句")

    def test_a_run(self):
        self.assertEqual(1, 1)

    def test_b_run(self):
        self.assertNotEqual(1, 2)

    def test_c_run(self):
        self.assertTrue(2 > 1)

    def test_d_run(self):
        self.assertIsNotNone(1)

if __name__ == "__main__":
    test_suit = unittest.TestSuite()
    #test_suit.addTest(MyTest("test_a_run"))
    test_suit.addTest(unittest.makeSuite(MyTest))
    with open("demo2.html", "wb") as fp:
        runner = HTMLTestRunner(stream = fp, title = "API测试报告", description = "测试情况")
        runner.run(test_suit)

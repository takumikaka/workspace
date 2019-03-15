# coding:UTF-8 -*-

import unittest
from test import Test

test = Test()

class MyTest(unittest.TestCase):

    def test_IsTrue(self):
        self.assertTrue(test.check_user("项少龙"))

if __name__ == "__main__":
    unittest.main(verbosity=2)

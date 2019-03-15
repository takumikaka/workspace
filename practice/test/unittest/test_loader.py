# coding:UTF-8 -*-

import unittest
from test_user_login import TestUserLogin

suit = unittest.TestLoader().loadTestsFromTestCase(TestUserLogin)

unittest.TextTestRunner(verbosity=2).run(suit)

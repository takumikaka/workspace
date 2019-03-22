# coding:UTF-8 -*-

import unittest

class Mytest(unittest.TestCase):
    def test_EqualOne(self):
        self.assertEqual(1, 2.0/2)

    def test_EqualTwo(self):
        self.assertEqual(1, True)

    def test_Is(self):
        self.assertIs(1, 2.0/2)

    def test_ListEqual(self):
        self.assertListEqual([1, 2], [1, 2])

    def test_DictEqual(self):
        self.assertDictEqual({"a": 1, "b": 2}, {"b":2, "a": 1})

    def test_IsNone(self):
        self.assertIsNone({})

    def test_False(self):
        self.assertFalse({})

    def test_In(self):
        self.assertIn("h", "hello")

    def test_Great(self):
        self.assertGreater(3, 2)

    def test_IsInstance(self):
        self.assertIsInstance({"a": 1, "b": 2}, dict)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""unittests for max_integer function"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestClass(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

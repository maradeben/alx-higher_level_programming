#!/usr/bin/python3
""" unittesting for Base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ functions to test the functionality of Base Class """
    def test_init(self):
        b = Base()
        self.assertIsInstance(b, Base)
        self.assertRaises(TypeError, Base, 3, 4)

    def test_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_non_empty_id(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        b_str = Base("str_id")
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b_str.id, "str_id")

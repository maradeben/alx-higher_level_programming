#!/usr/bin/python3
""" tests for the Rectangle class objects """
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ test the functionalities of the Rectangle Class """

    def test_init(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(5, 3)  # no args for x, y, and id
        r2 = Rectangle(5, 3, 3, 1)  # no args for id
        r3 = Rectangle(5, 3, 3, 1, 5)
        r4 = Rectangle(5, 3, 3, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 5)
        self.assertEqual(r4.id, 3)

        # test case with no arguments
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        err = "__init__() missing 2 required positional arguments: \
'width' and 'height'"
        self.assertEqual(str(e.exception), err)

        # test case with excessive arguments
        with self.assertRaises(TypeError) as e:
            r = Rectangle(3, 4, 5, 6, 7, 8)
        err = "__init__() takes from 3 to 6 positional arguments \
but 7 were given"
        self.assertEqual(str(e.exception), err)

    def test_setter_getter(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(5, 3)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)
        r1.width, r1.height = 7, 9
        r1.x, r1.y, r1.id = 2, 3, 55
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 9)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 55)

    def test_validator(self):
        Base._Base__nb_objects = 0
        self.assertEqual(True,
                         Rectangle.validator(Rectangle, 'width', 5, 'dim'))
        self.assertRaises(TypeError, Rectangle, 10, '2')
        self.assertRaises(TypeError, Rectangle, '10', 2)
        self.assertRaises(ValueError, Rectangle, 0, 5)
        self.assertRaises(ValueError, Rectangle, -5, 5)
        self.assertRaises(ValueError, Rectangle, 5, 0)
        self.assertRaises(ValueError, Rectangle, 5, -5)
        self.assertRaises(TypeError, Rectangle, 2, 3, 'x')
        self.assertRaises(TypeError, 2, 3, 4, 'y')
        r = Rectangle(10, 2)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -5)
        err = "x must be >= 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, -5)
        err = "y must be >= 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(ValueError) as e:
            r.width = -5
        err = "width must be > 0"
        self.assertEqual(str(e.exception), err)

        with self.assertRaises(TypeError) as e:
            r.width = "width"
        err = "width must be an integer"
        self.assertEqual(str(e.exception), err)

    def test_area(self):
        r = Rectangle(5, 8)
        self.assertEqual(r.area(), 40)

    @staticmethod
    def capture_stdout(rect, method):
        """ capture and return text printed to stdout """

        printout = io.StringIO()
        sys.stdout = printout
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return (printout)

    def test_display(self):
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        res = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), res)

        r = Rectangle(4, 6)
        printout = self.capture_stdout(r, "disp")
        self.assertEqual("####\n####\n####\n####\n####\n####\n",
                         printout.getvalue())

        r = Rectangle(4, 6, 2, 2)
        printout = self.capture_stdout(r, "disp")
        disp = """


          ####
          ####
          ####
          ####
          ####
          ####
        """

    def test__str__(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 5)
        info1 = "[Rectangle] (1) 0/0 - 4/5"
        self.assertEqual(str(r1), info1)
        r2 = Rectangle(8, 9, 3, 4, 99)
        info2 = "[Rectangle] (99) 3/4 - 8/9"
        self.assertEqual(str(r2), info2)

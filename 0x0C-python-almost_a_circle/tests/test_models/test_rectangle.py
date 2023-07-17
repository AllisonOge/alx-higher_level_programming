#!/usr/bin/python3
"""
module to test the rectangle class
"""
import unittest
from io import StringIO
import sys
from models.base import Base
from models.rectangle import Rectangle


def getprintedoutput(obj, method=None):
    """Returns the captured output to stdout for a given object

    Args:
        obj (class) : instance of a class
        method (str): method to be called
    """ 
    # redirect the stdout to StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # dynamically call the method on the object if method is not None
    if method is None:
        print(obj)
    else:
        obj_method = getattr(obj, method)
        obj_method()

    # get the value printed to stdout
    actual_output = captured_output.getvalue()

    # reset stdout to its original value
    sys.stdout = sys.__stdout__
    return actual_output

class TestRectangle(unittest.TestCase):
    """Test suite for the rectangle class"""
    def setUp(self):
        """set up before each test case"""
        Base._Base__nb_objects = 0  # reset before each test

    def tearDown(self):
        """clean up after each test case"""
        pass

    def test_instance_without_id(self):
        """test the instance with width and height properties"""
        r = Rectangle(12, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 4)

    def test_instance_with_id(self):
        """test the instance with width, height and id properties"""
        r = Rectangle(10, 2, id=10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_instance_with_x_y(self):
        """test the instance with x and y properties"""
        r = Rectangle(5, 2, 0, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 2)

    def test_instance_raise_typeerror(self):
        """test the instance raises TypeError with float types"""
        with self.assertRaises(TypeError):
            r = Rectangle(13.0, 3)
        with self.assertRaises(TypeError):
            r = Rectangle(13, 3.0)
        with self.assertRaises(TypeError):
            r = Rectangle(13, 3, x=0.0)
        with self.assertRaises(TypeError):
            r = Rectangle(13, 3, y=0.0)

    def test_instance_raises_valueerror(self):
        """test the instance raises ValueError with zero (except x and y) and
        negative values"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 3)
        with self.assertRaises(ValueError):
            r = Rectangle(-13, 3)
        with self.assertRaises(ValueError):
            r = Rectangle(13, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(13, -3)
        with self.assertRaises(ValueError):
            r = Rectangle(13, 3, x=-1)
        with self.assertRaises(ValueError):
            r = Rectangle(13, 3, y=-3)

    def test_area(self):
        """test that the instance computes its area"""
        r1 = Rectangle(7, 2)
        r2 = Rectangle(5, 3)
        r3 = Rectangle(3, 1)
        self.assertEqual(r1.area(), 14)
        self.assertEqual(r2.area(), 15)
        self.assertEqual(r3.area(), 3)

    def test_display(self):
        """test that the instance correctly prints the shape to stdout"""
        r1 = Rectangle(6, 2)
        r2 = Rectangle(2, 1, 3, 3)
        self.assertEqual(getprintedoutput(r1, "display"), "######\n######\n")
        self.assertEqual(getprintedoutput(r2, "display"), "\n\n\n   ##\n")


    def test_instance_print(self):
        """test that the instance correctly prints the formatted text"""
        r1 = Rectangle(2, 1, x=8, id=25)
        r2 = Rectangle(5, 2)
        actual_output1 = getprintedoutput(r1)
        actual_output2 = getprintedoutput(r2)
        self.assertEqual(actual_output1, "[Rectangle] (25) 8/0 - 2/1\n")
        self.assertEqual(actual_output2, "[Rectangle] (1) 0/0 - 5/2\n")

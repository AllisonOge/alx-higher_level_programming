#!/usr/bin/python3
"""
module to test the square class
"""
import unittest
from test_functions import getprintedoutput
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suite for the square class"""
    def setUp(self):
        """set up before each test case"""
        Base._Base__nb_objects = 0  # reset before each test

    def tearDown(self):
        """clean up after each test case"""
        pass

    def test_instance_without_id(self):
        """test the instance with size property"""
        s = Square(12, 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 12)
        self.assertEqual(s.width, 12)
        self.assertEqual(s.height, 12)

    def test_instance_with_id(self):
        """test the instance with size and id properties"""
        s = Square(10, id=10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_instance_with_x_y(self):
        """test the instance with x and y properties"""
        s = Square(5, 0, 2)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 2)

    def test_instance_raise_typeerror(self):
        """test the instance raises TypeError with float types"""
        with self.assertRaises(TypeError):
            s = Square(13.0)
        with self.assertRaises(TypeError):
            s = Square(13, x=0.0)
        with self.assertRaises(TypeError):
            s = Square(13, y=0.0)

    def test_instance_raises_valueerror(self):
        """test the instance raises ValueError with zero (except x and y) and
        negative values"""
        with self.assertRaises(ValueError):
            s = Square(0)
        with self.assertRaises(ValueError):
            s = Square(-13)
        with self.assertRaises(ValueError):
            s = Square(13, x=-1)
        with self.assertRaises(ValueError):
            s = Square(13, y=-3)

    def test_area(self):
        """test that the instance computes its area"""
        s1 = Square(7)
        s2 = Square(5)
        s3 = Square(3)
        self.assertEqual(s1.area(), 49)
        self.assertEqual(s2.area(), 25)
        self.assertEqual(s3.area(), 9)
    
    def test_display(self):
        """test that the instance correctly prints the shape to stdout"""
        s1 = Square(2)
        s2 = Square(2, 3, 3)
        self.assertEqual(getprintedoutput(s1, "display"), "##\n##\n")
        self.assertEqual(getprintedoutput(s2, "display"), "\n\n\n   ##\n   ##\n")
    
    def test_instance_print(self):
        """test that the instance correctly prints the formatted text"""
        s1 = Square(2, x=8, id=25)
        s2 = Square(5, 2)
        actual_output1 = getprintedoutput(s1)
        actual_output2 = getprintedoutput(s2)
        self.assertEqual(actual_output1, "[Square] (25) 8/0 - 2\n")
        self.assertEqual(actual_output2, "[Square] (1) 2/0 - 5\n")

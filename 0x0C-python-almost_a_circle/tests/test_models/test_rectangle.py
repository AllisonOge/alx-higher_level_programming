#!/usr/bin/python3
"""
module to test the rectangle class
"""
import unittest
from test_functions import getprintedoutput
from models.base import Base
from models.rectangle import Rectangle


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

    def test_update(self):
        """test that the instance correctlly updates its attributes"""
        r = Rectangle(3, 1, id=2003)
        r.update()
        self.assertEqual(getprintedoutput(r), "[Rectangle] (2003) 0/0 - 3/1\n")
        r.update(1)
        self.assertEqual(getprintedoutput(r), "[Rectangle] (1) 0/0 - 3/1\n")
        r.update(1, 5, 2, 1)
        self.assertEqual(getprintedoutput(r), "[Rectangle] (1) 1/0 - 5/2\n")
        r.update(height=3)
        self.assertEqual(getprintedoutput(r), "[Rectangle] (1) 1/0 - 5/3\n")
        r.update(id=2, x=0)
        self.assertEqual(getprintedoutput(r), "[Rectangle] (2) 0/0 - 5/3\n")
        with self.assertRaises(TypeError):
            r.update(width=5.0)
        with self.assertRaises(TypeError):
            r.update(height="1")
        with self.assertRaises(TypeError):
            r.update(x=[1,])
        with self.assertRaises(TypeError):
            r.update(y=(1,))
        with self.assertRaises(ValueError):
            r.update(width=0)
        with self.assertRaises(ValueError):
            r.update(x=-3)

    def test_to_dictionary(self):
        """
        test that the instance correctly returns the dictionary representation
        """
        r = Rectangle(3, 1)
        self.assertDictEqual(r.to_dictionary(), {'id': 1,
                                               'width': 3, 'height': 1,
                                               'x': 0, 'y':0})

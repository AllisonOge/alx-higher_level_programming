#!/usr/bin/python3
"""
module to test the rectangle class
"""
import unittest
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

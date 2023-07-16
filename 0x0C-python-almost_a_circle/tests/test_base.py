#!/usr/bin/python3
"""
module to test the base class
"""
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """Test suite for the base class"""
    def setUp(self):
        """set up before each test case"""
        Base._Base__nb_objects = 0  # reset before each test

    def tearDown(self):
        """clean up after each test case"""
        pass

    def test_instance_with_id(self):
        """test the instance id attribute is set correctly with id"""
        obj = Base(id=10)
        self.assertEqual(obj.id, 10)

    def test_instance_without_id(self):
        """test the instance id attribute is set to correctly without id"""
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

    def test_instance_id_increment(self):
        """test the id attribute increments correclty without id"""
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_instance_with_id_no_increment(self):
        """test the id attribute does not increment with id"""
        obj1 = Base()
        obj2 = Base(id=100)
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 100)
        self.assertEqual(obj3.id, 2)

#!/usr/bin/python3
"""
module to test the base class
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
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

    def test_to_json_string(self):
        """test that the Base class serialized a list of dictionaries"""
        r = Rectangle(3, 1)
        s = Square(5)
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([r.to_dictionary()]),
                         '[{"id": 1, "width": 3, "height": 1, "x": 0, "y": 0}]')
        self.assertEqual(Base.to_json_string([s.to_dictionary()]),
                         '[{"id": 2, "width": 5, "height": 5, "x": 0, "y": 0, "size": 5}]')
    
    def test_save_to_file(self):
        """test that JSON string is saved to file"""
        r = Rectangle(3, 1, id=200)
        s = Square(5)
        Rectangle.save_to_file([r.to_dictionary()])
        Square.save_to_file([s.to_dictionary()])
        # check if file exits 
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertTrue(os.path.exists("Square.json"))
        # check content of files
        with open("Rectangle.json", encoding="utf-8") as f:
            rectangle_content = f.read()
            self.assertEqual(rectangle_content, '[{"id": 200, "width": 3, "height": 1, "x": 0, "y": 0}]')
            
        with open("Square.json", encoding="utf-8") as f:
            square_content = f.read()
            self.assertEqual(square_content, '[{"id": 1, "width": 5, "height": 5, "x": 0, "y": 0, "size": 5}]')

        # remove test files
        os.remove("Rectangle.json")
        os.remove("Square.json")

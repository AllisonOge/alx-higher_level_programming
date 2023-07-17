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
        Rectangle.save_to_file([r])
        Square.save_to_file([s])
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

    def test_from_json_string(self):
        """test that the Base class deserialized a JSON string"""
        r = Rectangle(3, 1)
        s = Square(5)
        self.assertEqual(Base.from_json_string(None), "")
        self.assertDictEqual(Base.from_json_string('[{"id": 1, "width": 3, "height": 1, "x": 0, "y": 0}]')[0],
                         r.to_dictionary())
        self.assertDictEqual(Base.from_json_string('[{"id": 2, "width": 5, "height": 5, "x": 0, "y": 0, "size": 5}]')[0],
                         s.to_dictionary())
        
    def test_load_from_file(self):
        """test that JSON string is parsed to dictionary"""
        r1 = Rectangle(3, 1, id=200)
        s1 = Square(5)
        Rectangle.save_to_file([r1])
        Square.save_to_file([s1])
        r2 = Rectangle.load_from_file()
        s2 = Square.load_from_file()
        
        # check if list is not empty
        self.assertNotEqual(r2, [])
        self.assertNotEqual(s2, [])

        # check instances
        self.assertIsInstance(r2[0], Rectangle)
        self.assertIsInstance(s2[0], Square)

        # compare instances
        self.assertIsNot(r1, r2[0])
        self.assertNotEqual(r1, r2[0])
        self.assertIsNot(s1, s2[0])
        self.assertNotEqual(s1, s2[0])

        # remove test files
        os.remove("Rectangle.json")
        os.remove("Square.json")

        # check whe file does not exist
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_save_to_file_csv(self):
        """test that CSV string is saved to file"""
        r = Rectangle(3, 1, id=200)
        s = Square(5)
        Rectangle.save_to_file_csv([r])
        Square.save_to_file_csv([s])
        # check if file exits 
        self.assertTrue(os.path.exists("Rectangle.csv"))
        self.assertTrue(os.path.exists("Square.csv"))
        # check content of files
        with open("Rectangle.csv", encoding="utf-8") as f:
            rectangle_content = f.read()
            self.assertEqual(rectangle_content, 'id,width,height,x,y\n200,3,1,0,0\n')
            
        with open("Square.csv", encoding="utf-8") as f:
            square_content = f.read()
            self.assertEqual(square_content, 'id,width,height,x,y,size\n1,5,5,0,0,5\n')

        # remove test files
        os.remove("Rectangle.csv")
        os.remove("Square.csv")

    def test_load_from_file_csv(self):
        """test that CSV string is parsed to dictionary"""
        r1 = Rectangle(3, 1, id=200)
        s1 = Square(5)
        Rectangle.save_to_file_csv([r1])
        Square.save_to_file_csv([s1])
        r2 = Rectangle.load_from_file_csv()
        s2 = Square.load_from_file_csv()
        
        # check if list is not empty
        self.assertNotEqual(r2, [])
        self.assertNotEqual(s2, [])

        # check instances
        self.assertIsInstance(r2[0], Rectangle)
        self.assertIsInstance(s2[0], Square)

        # compare instances
        self.assertIsNot(r1, r2[0])
        self.assertNotEqual(r1, r2[0])
        self.assertIsNot(s1, s2[0])
        self.assertNotEqual(s1, s2[0])

        # remove test files
        os.remove("Rectangle.csv")
        os.remove("Square.csv")

        # check whe file does not exist
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

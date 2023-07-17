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

    def test_instance_print(self):
        """test that the instance correctly prints the formatted text"""
        s1 = Square(2, x=8, id=25)
        s2 = Square(5, 2)
        actual_output1 = getprintedoutput(s1)
        actual_output2 = getprintedoutput(s2)
        self.assertEqual(actual_output1, "[Square] (25) 8/0 - 2\n")
        self.assertEqual(actual_output2, "[Square] (1) 2/0 - 5\n")

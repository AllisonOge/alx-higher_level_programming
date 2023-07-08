#!/usr/bin/python3
"""
Test suite for max integer using unittest
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestMaxInteger class
    """
    def test_empty(self):
        """test empty list"""
        self.assertEqual(max_integer([]), None)

    def test_ordered_distinct_int(self):
        """test ordered distinct list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_ordered_distinct_float(self):
        """test ordered distinct list"""
        self.assertEqual(max_integer([1.0, 2.0, 3.0, 4.0]), 4.0)

    def test_unordered_distinct_int(self):
        """test unordered distinct list"""
        self.assertEqual(max_integer([4, 2, 1, 3]), 4)
    
    def test_unordered_distinct_float(self):
        """test unordered distinct list"""
        self.assertEqual(max_integer([4.0, 2.0, 1.0, 3.0]), 4)

    def test_repeating(self):
        """test repeating values list"""
        self.assertEqual(max_integer([1, 1.0, 1, 1.0]), 1.0)
    
    def test_max_in_the_middle(self):
        """test maximum number in the middle"""
        self.assertEqual(max_integer([1.0, float('inf'), 23]), float('inf'))
    
    def test_at_least_one_negative(self):
        """test distinct values list"""
        self.assertEqual(max_integer([-14.1, -5.5, -7, 1.0]), 1.0)

    def test_only_negative(self):
        """test distinct negative values list"""
        self.assertEqual(max_integer([-14.1, -5.5, -7, -11]), -5.5)
    
    def test_one_element(self):
        """test distinct values list"""
        self.assertEqual(max_integer([-14.1]), -14.1)

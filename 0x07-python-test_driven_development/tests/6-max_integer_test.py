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

    def test_unordered_distinct_int(self):
        """test unordered distinct list"""
        self.assertEqual(max_integer([4, 2, 1, 3]), 4)

    def test_repeating_int(self):
        """test repeating values list"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_ordered_distinct_float(self):
        self.assertEqual(max_integer([1.0, 2.0, 3.0, 4.0]), 4.0)

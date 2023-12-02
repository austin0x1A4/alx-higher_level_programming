#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_normal_list(self):
        """Test with a normal list of ints"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)
    
    def test_one_element(self):
        """Test list with one element""" 
        self.assertEqual(max_integer([5]), 5)
    
    def test_floats(self):
        """Test a list of floats"""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)
    
    def test_ints_and_floats(self):
        """Test a list of ints and floats"""
        self.assertEqual(max_integer([1, 2, 3.3, 4.5]), 4.5)
        
    def test_string(self):
        """Test string argument"""
        with self.assertRaises(TypeError):
            max_integer("hello")
            
if __name__ == '__main__':
    unittest.main()

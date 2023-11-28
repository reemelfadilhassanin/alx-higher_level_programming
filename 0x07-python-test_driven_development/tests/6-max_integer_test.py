#!/usr/bin/python3
"""Unittest for the function max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer."""

    def test_max_empty(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_max_of_float(self):
        """Test floats list"""
        f = [2.9, 8.8, 7.1, 10.99]
        self.assertEqual(max_integer(f), 10.99)

    def test_float_negative(self):
        """Test negative floats number"""
        self.assertEqual(max_integer([-9.0, -3.4, -0.1]), -0.1)

    def test_max_int(self):
        """Test for int number in not order way and return the max int of list"""
        value = max_integer([20, 18, 3])
        self.assertEqual(value, 20)

    def test_regular_int(self):
        """Test for int number in ordereslist and return the max int of list"""
        value = max_integer([10, 11, 12, 13])
        self.assertEqual(value, 13)

    def test_max_negative(self):
        """Test negative values in order way"""
        neg = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(neg, -1)

    def test_max_negative_not_order(self):
        """Test negative values in not order way"""
        neg = max_integer([-3, -10, -5, -13, -50])
        self.assertEqual(neg, -3)

    def test_max_duplicate(self):
        """Test if exit duplicate values and return max"""
        dup = max_integer([5, 5, 3, 4, 5])
        self.assertEqual(dup, 5)

    def test_max_neg_duplicate(self):
        """Test if exit duplicate negative values and return max"""
        dup = max_integer([-5, -5, 7, -6, -5])
        self.assertEqual(dup, -5)

    def test_max_negative_not_order(self):
        """Test negative values in not order way"""
        neg = max_integer([-3, -10, -5, -13, -50])
        self.assertEqual(neg, -3)

    def test_max_identical(self):
        """Test max of identical values"""
        result = max_integer([1, 1, 1, 1])
        self.assertEqual(result, 1)

    def test_max_identical_float(self):
        """Test max of identical values of float list"""
        result = max_integer([1.22, 1.22, 1.22, 1.22])
        self.assertEqual(result, 1.22)

    def test_max_duplicate_float(self):
        """Test if exit duplicate float values and return max"""
        dup = max_integer([4.0, 3.5, 4.0, 2.0, 4.0])
        self.assertEqual(dup, 4.0)

    def test_max_negative_duplicate_float(self):
        """Test if exit duplicate negative float values and return max"""
        dup = max_integer([-5.0, -5.0, -8.2, -9.1, -5.0])
        self.assertEqual(dup, -5.0)

    def test_max_of_mix_int_float(self):
        """Test mixed vlaue of int and float and return max"""
        dup = max_integer([5, 9.0, 7.0, 1, 10])
        self.assertEqual(dup, 10)

    def test_max_of_mix_negative_int_float(self):
        """Test mixed nagativevlaue of int and float and return max"""
        dup = max_integer([-5, -9.0, -7.0, -1, -10])
        self.assertEqual(dup, -1)

    def test_max_of_long(self):
        """Test long int and return max value  of list"""
        value = max_integer([5000000, 1000000, 2000000])
        self.assertEqual(value, 5000000)

    def test_not_int(self):
        """Test list of non-ints and ints should raise a TypeError exception"""
        value = ["foo", "a", 10, 78]
        self.assertRaises(TypeError, max_integer, value)

    def test_max_of_single_value(self):
        """Return max of sigle element"""
        single = max_integer([5])
        self.assertEqual(single, 5)

    def test_max_not_list(self):
        """Test max with parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 13)

    def test_max_of_strings(self):
        """Test max vlaue with the list of strings: should return the first string"""
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 3, 2, 1]), 9)

    def test_one_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-10, 0, 100, -30]), 100)

    def test_all_same(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.14, 2.0]), 3.14)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 3, 4.75]), 4.75)

    def test_string_input(self):
        self.assertEqual(max_integer("Holberton"), 't')

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["a", "z", "x", "y"]), "z")

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            max_integer(1234)


if __name__ == '__main__':
    unittest.main()

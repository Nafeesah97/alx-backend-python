#!/usr/bin/env python3
"""test utils"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A class to test the access nested map function ghjk"""
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """Test that the method returns what it is supposed to"""
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected_value)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in {'a': 1}")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        """Test that the method raises KeyError with correct message"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        
        self.assertEqual(str(context.exception), expected_message)

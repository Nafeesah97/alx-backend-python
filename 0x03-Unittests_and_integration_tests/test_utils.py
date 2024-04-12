#!/usr/bin/env python3
"""test utils"""
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json
from unittest.mock import patch


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
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_message):
        """Test that the method raises KeyError with correct message"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """
    To test the get json method
    
    Method:
        test_get_json():
        to test that utils.get_json returns the expected result
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])

    def test_get_json(self, url, expected_value):
        """To test get_json method of utils"""
        with patch(get_json) as test_get_json:
            response = test_get_json(url)
        test_get_json.assert_called_once_with(url)
        self.assertEqual(response, expected_value)

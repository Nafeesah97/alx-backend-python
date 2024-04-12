#!/usr/bin/env python3
"""test utils"""
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


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
        mock_res = Mock()
        mock_res.json.return_value = expected_value
        with patch('utils.requests.get') as test_get_json:
            test_get_json.return_value = mock_res
            response = get_json(url)
            test_get_json.assert_called_once_with(url)
            self.assertEqual(response, expected_value)


class  TestMemoize(unittest.TestCase):
    """
    To test the memoize function in the utils class
    """

    def test_memoize(self):
        """Testing the memooize function"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        

        mock_res = Mock()
        with patch('TestClass.a_method') as res:
            res.return_value = mock_res
            first_call = TestClass.a_property()
            second_call = TestClass.a_property()
            res.assert_called_once()

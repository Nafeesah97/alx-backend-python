#!/usr/bin/env python3
"""test utils"""
from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """
    A class that contains the tests
    for GithubOrgClient methods
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('GithubOrgClient.get_json')
    def test_org(self, org_name, mock_res):
        """test that GithubOrgClient.org returns the correct value"""
        ORG_URL = f"https://api.github.com/orgs/{org_name}"
        
        client = GithubOrgClient(org_name)

        org_result = client.org()

        mock_res.assert_called_once_with(ORG_URL)

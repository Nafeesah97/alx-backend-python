#!/usr/bin/env python3
"""test utils"""
from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """
    A class that contains the tests
    for GithubOrgClient methods
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_res):
        """test that GithubOrgClient.org returns the correct value"""
        ORG_URL = f"https://api.github.com/orgs/{org_name}"
        
        client = GithubOrgClient(org_name)

        org_result = client.org()

        mock_res.assert_called_once_with(ORG_URL)

    def test_public_repos_url(self):
        """method to unit-test GithubOrgClient._public_repos_url"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

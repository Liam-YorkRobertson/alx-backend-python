#!/usr/bin/env python3
"""
creating tests for the client file
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock, PropertyMock
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    tests GithubOrgClient
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, response_data: Dict,
                 mocked_function: Mock) -> None:
        mocked_function.return_value = Mock(return_value=response_data)
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org(), response_data)
        mocked_function.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mocked_property: Mock) -> None:
        mocked_property.return_value = {'repos_url': "https://api.github."
                                        "com/users/google/repos"}
        github_org_client = GithubOrgClient("google")
        self.assertEqual(github_org_client._public_repos_url,
                         "https://api.github.com/users/google/repos")


if __name__ == '__main__':
    unittest.main()

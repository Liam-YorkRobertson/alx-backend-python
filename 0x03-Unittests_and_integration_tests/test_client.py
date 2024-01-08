#!/usr/bin/env python3
"""
creating tests for the client file
"""
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, Mock, PropertyMock
from typing import Dict
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch("client.GithubOrgClient._public_repos_url",
           new_callable=PropertyMock)
    @patch("client.get_json")
    def test_public_repos(self, mock_get_json, mock_public_repos_url):
        mock_get_json.return_value = [{"name": "repo1"}]
        mock_public_repos_url.return_value = ("https://api.github.com"
                                              "/users/google/repos")

        github_org_client = GithubOrgClient("google")
        repos = github_org_client.public_repos()

        expected_repos = ["repo1"]
        self.assertEqual(repos, expected_repos)
        mock_get_json.assert_called_once_with("https://api.github.com"
                                              "/users/google/repos")
        mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict, license_key: str,
                         expected_result: bool) -> None:
        github_org_client = GithubOrgClient("test_org")
        result = github_org_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    integration tests for GithubOrgClient
    """
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            Mock(json=lambda: cls.org_payload),
            Mock(json=lambda: cls.repos_payload),
            Mock(json=lambda: cls.apache2_repos),
        ]

    def test_public_repos_integration(self):
        github_org_client = GithubOrgClient("test_org")
        repos = github_org_client.public_repos()

        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        github_org_client = GithubOrgClient("google")
        first_repo = github_org_client.repos_payload[0]
        github_org_client._repos_payload = first_repo
        with patch.object(GithubOrgClient, 'repos_payload', return_value=None):
            self.assertEqual(
                github_org_client.public_repos(license="apache-2.0"),
                self.apache2_repos,
            )

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()

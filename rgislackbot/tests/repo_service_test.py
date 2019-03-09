import unittest
from unittest.mock import MagicMock
from rgislackbot.repo_command.repo_service import RepoService
from rgislackbot.repo_command.github_api.api import Api

class repo_service_test(unittest.TestCase):
    def test_repo_service_start_command_returns_Invalid_command_not_enough_params(self):
        uut = RepoService()
        result = uut.start_command("Command")
        self.assertEqual("Invalid command", result)

    def test_repo_service_start_command_returns_Invalid_command_bad_params(self):
        uut = RepoService()
        result = uut.start_command("My Command")
        self.assertEqual("Invalid command", result)

    def test_repo_service_calls_api_pull_requests(self):
        uut = RepoService()
        mock_api = Api()
        mock_api.pull_requests = MagicMock()
        uut.api = mock_api
        uut.start_command("repo pull-requests")
        mock_api.pull_requests.assert_called_with()
        
    def test_repo_service_calls_api_pull_requests_with_number(self):
        uut = RepoService()
        mock_api = Api()
        mock_api.pull_requests = MagicMock()
        uut.api = mock_api
        uut.start_command("repo pull-requests 123")
        mock_api.pull_requests.assert_called_with('123')

if __name__ == '__main__': 
    unittest.main()
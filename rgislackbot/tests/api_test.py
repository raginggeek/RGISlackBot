import unittest
from unittest.mock import MagicMock
from rgislackbot.repo_command.github_api.api import Api
from rgislackbot.repo_command.github_api.urls import Urls

class api_test(unittest.TestCase):

    @unittest.mock.patch('requests.get')
    def test_api_pull_requests_call_url(self, request_mock):
        mock_response = MagicMock()
        request_mock.return_value= mock_response
        mock_response.text = 'My Json Value'
        uut = Api()

        urls = Urls()
        uut.pull_requests()
        request_mock.assert_called_with(urls.pull_requests)
        
    @unittest.mock.patch('requests.get')
    def test_api_pull_requests_call_url_with_number(self, request_mock):
        mock_response = MagicMock()
        request_mock.return_value= mock_response
        mock_response.text = 'My Json Value'
        uut = Api()

        urls = Urls()
        uut.pull_requests('123')
        request_mock.assert_called_with('{0}{1}'.format(urls.pull_requests, 123))
        
    def test_api_pull_requests_throws_exception(self):
        uut = Api()
        with self.assertRaises(Exception) as context:
            uut.pull_requests('asdf')

        self.assertTrue('Requested pull number must be numeric' in str(context.exception))
        

if __name__ == '__main__': 
    unittest.main()
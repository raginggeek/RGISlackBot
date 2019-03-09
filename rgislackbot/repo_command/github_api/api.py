import requests
from rgislackbot.repo_command.github_api.urls import Urls

class Api(object):
    def __init__(self):
        self.urls = Urls()

    def pull_requests(self, request_number = None):
        url = self.urls.pull_requests

        if request_number != None:
            if request_number.isdigit() == False:
                raise Exception('Requested pull number must be numeric')
            url = url + request_number

        response = requests.get(url)
        return response.json()

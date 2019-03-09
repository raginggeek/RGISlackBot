from rgislackbot.repo_command.github_api.api import Api

class RepoService(object):
    def __init__(self):
        self.api = Api()

    def start_command(self, command):
        command_list = command.split()
        param_count = len(command_list)

        response = "Invalid command"

        if param_count > 1:
            if command_list[1] == 'pull-requests':
                if param_count > 2:
                    response = self.api.pull_requests(command_list[2])
                else:
                    response = self.api.pull_requests()

        return response

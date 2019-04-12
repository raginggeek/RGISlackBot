class Demo:
    RESPONSE = "This is an example response, please code additional responses."

    def __init__(self, slack_client, config):
        self.slack_client = slack_client
        self.config = config

    def handle_command(self, command, channel):
        # command is unused here
        print(command)
        self.slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=self.RESPONSE
        )

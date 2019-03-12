import re

from rgislackbot.dellystuff.bf5stats import BF5DataHandler


class EventHandler:
    MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

    def __init__(self, username, slack_client):
        # TODO: initialize some dictionaries by reading config files or something to establish what commands belong
        # TODO: to which module.
        self.username = username
        self.slack_client = slack_client
        self.bf5 = None

    def handle_events(self, events):
        command, channel = self.parse_bot_commands(events)
        if command:
            self.handle_command(command, channel)

    def parse_bot_commands(self, slack_events):
        """
            Parses a list of events coming from the Slack RTM API to find bot commands.
            If a bot command is found, this function returns a tuple of command and channel.
            If its not found, then this function returns None, None.
        """
        for event in slack_events:
            if event["type"] == "message" and "subtype" not in event:
                user_id, message = self.parse_direct_mention(event["text"])
                if user_id == self.username:
                    return message, event["channel"]
        return None, None

    def parse_direct_mention(self, message_text):
        """
            Finds a direct mention (a mention that is at the beginning) in message text
            and returns the user ID which was mentioned. If there is no direct mention, returns None
        """
        matches = re.search(self.MENTION_REGEX, message_text)
        # the first group contains the username, the second group contains the remaining message
        return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

    def handle_command(self, command, channel):
        """
            Executes bot command if the command is known
        """
        # Default response is help text for the user
        # default_response = "Not sure what you mean. Try *{}*.".format("HI")

        # Finds and executes the given command, filling in response
        # response = None

        # TODO: we need to make the code more robust and route items in command lists to their appropriate handlers
        if command.startswith("BF5"):
            # Pass in the command and slack connection and the class can parse it from there
            if self.bf5 == None:
                self.bf5 = BF5DataHandler(self.slack_client)
            self.bf5.handle_bf5_request(command, channel)

        ''' self.slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response or default_response
        )'''

import re
from pydoc import locate

from rgislackbot.dispatcher.dispatchconfig import DispatchConfig


class EventHandler:
    MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
    CONFIG_ELEMENT = "dispatcher"

    def __init__(self, username, slack_client, config):
        """
        :param str username:
        :param Slack_Client slack_client:
        :param Configurator config:
        """
        self.username = username
        self.slack_client = slack_client
        self.config = config
        self.dispatch_config = DispatchConfig(config.get_config(self.CONFIG_ELEMENT))
        self.handlers = {}

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
        default_response = "Not sure what you mean. Try *{}*.".format("HI")

        # Finds and executes the given command, filling in response
        handler = self.dispatch_config.get_handler_by_command(command.split(None, 1)[0])
        if handler is None:
            print("unrecognized command detected: " + command.split(None, 1)[0])
            # Sends the response back to the channel
            self.slack_client.api_call(
                "chat.postMessage",
                channel=channel,
                text=default_response
            )
        else:
            print("using: " + handler["fullpath"] + " to handle the request")
            if handler["class"] in self.handlers:
                self.handlers[handler["class"]].handle_command(command, channel)
            else:
                cls = locate(handler["fullpath"])
                print(cls)
                self.handlers[handler["class"]] = cls(self.slack_client, self.config)
                self.handlers[handler["class"]].handle_command(command, channel)

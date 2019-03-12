import json
import urllib.error
import urllib.parse
import urllib.request


class BF5DataHandler:
    # Central handler class for BF5 stuff
    def __init__(self, slack_client):
        self.slack_client = slack_client

    # This is just a single function for now. It will be expanded based on the command later
    def handle_bf5_request(self, command, channel):
        self.show_player_stats(command, channel)

    # This class handles gathering and displaying a player's stats specifically

    # Builds a table of basic stats and returns it as a string
    # Arguments: JSON to parse
    @staticmethod
    def parse_stats_into_table(data):
        return "```Deaths: " + str(data["data"]["stats"]["deaths"]["value"]) + "```"

    # Gets the PSN name and displays basic BF5 stats
    # Arguments: Connection to Slack client, string of command, default output channel
    def show_player_stats(self, command, channel):
        # Default response is help text for the user
        default_response = "Incorrect input. Try BF5 [public] PSNName (PSN names are case sensitive)"

        # Divide command to look for parameters
        command_list = command.split()
        # TODO Parameters: compare with another player, store psn name and associate with Slack handle
        # Get the last parameter as the player's username
        player = command_list[-1]
        # Flag for whether the result should be shown in the channel. If not, it is DMed instead.
        public = "public" in command_list

        # URL for fetching the JSON data from Battlefield Tracker
        url_json = "https://api.battlefieldtracker.com/api/v1/bfv/profile/psn/" + player

        # Request from URL. The user agent is necessary or else it returns a 403 error
        req = urllib.request.Request(
            url_json,
            data=None,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        )

        # Decode JSON into data object
        try:
            with urllib.request.urlopen(req) as url:
                data = json.loads(url.read().decode())

            if not public:
                channel = "@user"

            # Build a string from the data object
            slack_response = self.parse_stats_into_table(data)

        except urllib.error.HTTPError:
            slack_response = "```Error. HTTP error connecting to Battlefield Tracker```"
        except urllib.error.URLError:
            slack_response = "```Error. Check the PSN name (case sensitive) and try again.```"

        # Sends the response back to the channel
        self.slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=slack_response or default_response
        )

# Fancy EOF line

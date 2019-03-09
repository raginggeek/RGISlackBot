from unittest.mock import MagicMock

from slackclient import SlackClient

from rgislackbot.dispatcher.eventhandler import EventHandler


class TestEventHandler:

    def test_instance(self):
        slack_client = SlackClient()
        slack_client.api_call = MagicMock(return_value=None)
        event_handler = EventHandler("Ufoo", slack_client)
        assert type(event_handler) is EventHandler

    def test_hi_response(self):
        slack_client = SlackClient()
        slack_client.api_call = MagicMock(return_value=None)
        event_handler = EventHandler("Ufoo", slack_client)
        event_handler.handle_events([{"type": "message", "channel": "foothings", "text": "<@Ufoo> HI"}])
        slack_client.api_call.assert_called_with("chat.postMessage", channel="foothings",
                                                 text="Sure...write some more code then I can do that!")

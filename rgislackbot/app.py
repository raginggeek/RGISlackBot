import os
import time

from slackclient import SlackClient

from rgislackbot.dispatcher.eventhandler import EventHandler

# constants
RTM_READ_DELAY = 1  # 1 second between reads


def run():
    """
    main executable loop, will continue to read events off the stack and feed the dispatcher until exited.
    """
    # instantiate the slack client
    slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

    if slack_client.rtm_connect(with_team_state=False):
        event_handler = EventHandler(slack_client.api_call("auth.test")["user_id"], slack_client)
        print("RGISlackBot Up and Running")
        while True:
            event_handler.handle_events(slack_client.rtm_read())
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed Exception traceback printed above.")

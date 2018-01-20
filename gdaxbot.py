import json
import os
import time
import re
import urllib2
from slackclient import SlackClient

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

# gdaxbot's user ID in Slack: value is assigned after the bot starts up
gdaxbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM

CURRENCY_BTC = "BTC"
CURRENCY_ETH = "ETH"
CURRENCY_LTC = "LTC"
CURRENCY_BCH = "BCH"
SUPPORTED_CURRENCY = [CURRENCY_BTC, CURRENCY_ETH, CURRENCY_LTC, CURRENCY_BCH]

SAMPLE_COMMAND = "price LTC or PRICE btc or Price Eth"
SUPPORTED_COMMANDS = ["PRICE"]

# Default response is help text for the user
DEFAULT_RESPONSE = "Not sure what you mean. Try *{}*.".format(SAMPLE_COMMAND)
MENTION_REGEX = "^<@(|[WU].+)>(.*)"

GDAX_API = {
    "BTC" : "https://api.gdax.com/products/BTC-USD/ticker",
    "ETH" : "https://api.gdax.com/products/ETH-USD/ticker",
    "LTC" : "https://api.gdax.com/products/LTC-USD/ticker",
    "BCH" : "https://api.gdax.com/products/BCH-USD/ticker"
}

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == gdaxbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def get_gdax_price(command, currency):
    request_call = urllib2.urlopen(GDAX_API[currency], timeout=60)
    reponse_dump = json.load(request_call)
    return "1 {0} is {1} USD".format(str(currency), reponse_dump[str(command).lower()])

def show_response_on_slack(response_str):
    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response_str)

def handle_command(command_str, channel):
    """
        Executes bot command if the command is known
    """
    command_list = command_str.split(" ")
    if len(command_list) is not 2:
        show_response_on_slack(DEFAULT_RESPONSE)
    else:
        command_attribute = command_list[0]
        command_currency = command_list[1]

        if command_attribute not in SUPPORTED_COMMANDS or command_currency not in SUPPORTED_CURRENCY:
            show_response_on_slack(DEFAULT_RESPONSE)
        else:
            response = get_gdax_price(command_attribute, command_currency)
            show_response_on_slack(response)


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        gdaxbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(str(command).upper(), channel)
            else:
                # Sends the response back to the channel
                slack_client.api_call(
                    "chat.postMessage",
                    channel=channel,
                    text= "Command missing, Try *{0}*".format(SAMPLE_COMMAND)
                )

            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
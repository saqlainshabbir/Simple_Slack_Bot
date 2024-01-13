import slack
import os
from dotenv import load_dotenv
from datetime import date
import time

env_path = ".env"
load_dotenv(env_path)

client = slack.WebClient(os.environ["SLACK_BOT_TOKEN"])

t = time.localtime()
current_time = time.strftime("%H:%H:%S", t)
client.chat_postMessage(channel="general", text="The current date is " + str(date.today()) + " " + str(current_time))

import tweepy
import time

import os

API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
BEARER_TOKEN = os.environ['BEARER_TOKEN']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

minutes = 1

while True:
    if minutes  == 1:
        mensagem = f"Passou {minutes} minute"
    else:
        mensagem = f"has passed.  {minutes} minutes"
    
    client.create_tweet(text=mensagem)
    print(f"Tweet {minutes} postado!")
    
    minutes += 1
    time.sleep(60)

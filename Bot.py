import tweepy
import time

API_KEY = "NJxVWrRUwMFc0y9ssclVoMWc3"
API_SECRET = "CnKw9IdeV2f1ka9ZAPRZeQlyiwIRPgWrXM8kcMg897c4Z5rAqR"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADHZ6gEAAAAADd10pSPLc%2FV2l%2Bf4MZK4EOy6waY%3DiFjdneYgC7AM7dhDD0XLPUKm4OXP3SloKHa6Ig9xcIwtOVz4GJ"
ACCESS_TOKEN = "2007259782147911680-nrC3df7SpukYOcJzkesDzO1G8GVTq4"
ACCESS_TOKEN_SECRET = "jYqFqgAQcsSjXaFNOSWE9CQ2pvAAodJctePKxpn2GkKFc"

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

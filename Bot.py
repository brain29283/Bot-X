import tweepy
import time
import os

# Pega as credenciais dos Secrets
API_KEY = os.environ.get('API_KEY')
API_SECRET = os.environ.get('API_SECRET')
BEARER_TOKEN = os.environ.get('BEARER_TOKEN')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

# Conecta no X
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Inicia o contador
minutes = 1

# Loop infinito postando a cada minuto
while True:
    try:
        if minutes == 1:
            message = f"{minutes} minute has passed"
        else:
            message = f"{minutes} minutes have passed"
        
        client.create_tweet(text=message)
        print(f"✅ Tweet {minutes} posted!")
        
        minutes += 1
        time.sleep(60)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        time.sleep(60)

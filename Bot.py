import tweepy
import time
from flask import Flask
from threading import Thread

# Servidor web para manter ativo
app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Bot is running! ✅"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Credenciais do X
API_KEY = "Gil5u03fBg24n6n20XCC3tTUe"
API_SECRET = "rJWAityGrdkiUj6n7xZUHQqb8Q4dVqt6x6GJkkly1obQWy8Az6"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADHZ6gEAAAAA%2FYHQtlLuA3Ug3dH0077rH%2F5Bn5Q%3DyXlQ8wenKCaoveVvjGQKXLzCbxnOmOyE43uzZ5LIwJiL95mBJh"
ACCESS_TOKEN = "2007259782147911680-oBgDV6nwrLOqVzRQhCKs6WfV5FmgZb"
ACCESS_TOKEN_SECRET = "80MZTfiC8wIKfqZyptz8dPEJVuo2UY6KYlz1XdNAut6Jc"

# Conecta no X
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Função do bot
def run_bot():
    minutes = 1
    while True:
        try:
            if minutes == 1:
                message = f"{minutes} minute has passed"
            else:
                message = f"{minutes} minutes have passed"
            
            client.create_tweet(text=message)
            print(f"✅ Tweet {minutes} posted!")
            
            minutes += 5
            time.sleep(60)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(300)

# Inicia tudo
if __name__ == "__main__":
    Thread(target=run_flask).start()
    print("🌐 Flask server started!")
    print("🤖 Bot started!")
    run_bot()

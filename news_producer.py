# news_producer.py
# Streams news headlines from NewsAPI into Kafka
import requests
from kafka import KafkaProducer
import json
import time
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_API_URL = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def fetch_latest_headlines():
    response = requests.get(NEWS_API_URL)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        for article in articles:
            yield {
                'title': article.get('title'),
                'description': article.get('description'),
                'url': article.get('url'),
                'publishedAt': article.get('publishedAt')
            }
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return []

def produce_news():
    print("Fetching and sending news headlines to Kafka...")
    for news_item in fetch_latest_headlines():
        producer.send('news-topic', news_item)
        print(f"Sent: {news_item['title']}")
        time.sleep(1)  # Throttle to avoid spamming
    producer.flush()
    print("Done sending headlines.")

if __name__ == "__main__":
    produce_news()

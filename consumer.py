# consumer.py
# Kafka Consumer Example
from kafka import KafkaConsumer
from pymongo import MongoClient
import json
from collections import Counter
import nltk
from nltk.corpus import stopwords
import string

# Download NLTK stopwords if not already present
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    import nltk
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['news']
headlines_collection = db['headlines']

consumer = KafkaConsumer(
    'news-topic',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='news-group'
)

def consume_messages():
    print("Listening for messages...")
    keyword_counter = Counter()
    processed_count = 0
    for message in consumer:
        news = message.value
        title = news.get('title') or ''
        print(f"\nTitle: {title}")
        print(f"Description: {news.get('description')}")
        print(f"Published At: {news.get('publishedAt')}")
        print(f"URL: {news.get('url')}")
        headlines_collection.insert_one(news)
        print("Saved to MongoDB.")

        # --- Analytics: keyword counting ---
        # Tokenize, lowercase, remove punctuation and stopwords
        words = [
            word.lower().strip(string.punctuation)
            for word in title.split()
            if word.lower() not in stop_words and word.isalpha()
        ]
        keyword_counter.update(words)
        processed_count += 1

        # Print top 5 keywords every 5 headlines
        if processed_count % 5 == 0:
            print("\nTop 5 Keywords so far:")
            for word, count in keyword_counter.most_common(5):
                print(f"{word}: {count}")

if __name__ == "__main__":
    consume_messages()

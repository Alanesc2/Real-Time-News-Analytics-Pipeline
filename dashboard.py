# dashboard.py
# Streamlit dashboard for real-time news analytics
import streamlit as st
from pymongo import MongoClient
from collections import Counter
import pandas as pd

from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=10 * 1000)  # Refresh every 10 seconds

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['news']
headlines_collection = db['headlines']

st.title("Real-Time News Analytics Dashboard")

# Fetch latest headlines
def get_latest_headlines(n=10):
    return list(headlines_collection.find().sort('publishedAt', -1).limit(n))

# Fetch all headlines for analytics
def get_all_titles():
    return [doc.get('title', '') for doc in headlines_collection.find() if doc.get('title')]

# Keyword analytics
def get_top_keywords(titles, top_n=10):
    import nltk
    from nltk.corpus import stopwords
    import string
    try:
        stop_words = set(stopwords.words('english'))
    except LookupError:
        nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))
    counter = Counter()
    for title in titles:
        words = [
            word.lower().strip(string.punctuation)
            for word in title.split()
            if word.lower() not in stop_words and word.isalpha()
        ]
        counter.update(words)
    return counter.most_common(top_n)

# Layout
st.header("Latest Headlines")
latest = get_latest_headlines(10)
for doc in latest:
    st.write(f"**{doc.get('title', 'No Title')}**")
    st.caption(doc.get('publishedAt', ''))
    st.write(doc.get('description', ''))
    st.write(f"[Read more]({doc.get('url', '')})")
    st.markdown('---')

st.header("Top Keywords")
titles = get_all_titles()
top_keywords = get_top_keywords(titles, top_n=10)
if top_keywords:
    df = pd.DataFrame(top_keywords, columns=['Keyword', 'Count'])
    st.bar_chart(df.set_index('Keyword'))
else:
    st.write("No keywords to display yet.")

st.caption("Dashboard auto-refreshes every 10 seconds.")

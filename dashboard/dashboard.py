# dashboard.py
# Streamlit dashboard for real-time news analytics
import streamlit as st
from pymongo import MongoClient
from collections import Counter
import pandas as pd
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=10 * 1000)

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['news']
headlines_collection = db['headlines']

st.title("Real-Time News Analytics Dashboard")

# --- Data Loading and Filtering ---
# Load all headlines into a DataFrame for filtering and analytics
all_docs = list(headlines_collection.find())
df = pd.DataFrame(all_docs)

# --- Source Filter ---
sources = sorted(df['source'].dropna().unique()) if 'source' in df else []
selected_source = st.selectbox("Filter by Source", options=["All"] + sources)

filtered_df = df.copy()
if selected_source != "All":
    filtered_df = filtered_df[filtered_df['source'] == selected_source]

# --- Category Filter (if available) ---
categories = []
if 'category' in filtered_df:
    categories = sorted(filtered_df['category'].dropna().unique())
if categories:
    selected_category = st.selectbox("Filter by Category", options=["All"] + categories)
    if selected_category != "All":
        filtered_df = filtered_df[filtered_df['category'] == selected_category]

# --- Latest Headlines ---
st.header("Latest Headlines")
latest = filtered_df.sort_values('publishedAt', ascending=False).head(10)
for _, doc in latest.iterrows():
    st.write(f"**{doc.get('title', 'No Title')}**")
    st.caption(str(doc.get('publishedAt', '')))
    st.write(doc.get('description', ''))
    st.write(f"[Read more]({doc.get('url', '')})")
    st.markdown('---')

# --- Top Keywords ---
st.header("Top Keywords")
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

titles = filtered_df['title'].dropna().tolist()
top_keywords = get_top_keywords(titles, top_n=10)
if top_keywords:
    df_keywords = pd.DataFrame(top_keywords, columns=['Keyword', 'Count'])
    st.bar_chart(df_keywords.set_index('Keyword'))
else:
    st.write("No keywords to display yet.")

# --- Sentiment Analysis ---
st.header("Headline Sentiment Breakdown")
if 'sentiment' in filtered_df:
    sentiment_counts = filtered_df['sentiment'].value_counts()
    sentiment_df = sentiment_counts.reset_index()
    sentiment_df.columns = ['Sentiment', 'Count']
    st.dataframe(sentiment_df, hide_index=True)
else:
    st.write("No sentiment data available.")

# --- Time Series Analytics ---
st.header("Headline Counts Over Time")
if 'publishedAt_dt' in filtered_df:
    # Convert to datetime if not already
    filtered_df['publishedAt_dt'] = pd.to_datetime(filtered_df['publishedAt_dt'], errors='coerce')
    time_series = filtered_df.set_index('publishedAt_dt').resample('1H').size()
    st.line_chart(time_series)
else:
    st.write("No time series data available.")

st.caption("Dashboard auto-refreshes every 10 seconds.")

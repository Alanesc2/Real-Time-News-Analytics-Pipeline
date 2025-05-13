# Real-Time News Analytics Pipeline (Kafka, MongoDB, Streamlit)

This project ingests live news headlines from NewsAPI, streams them through Kafka, stores them in MongoDB, and visualizes real-time analytics on a Streamlit dashboard.

## Features
- Real-time news ingestion (NewsAPI)
- Kafka-based message brokering
- MongoDB storage
- Keyword analytics
- Live dashboard (Streamlit)
- Docker Compose for local development
- Environment variable support with `.env`

## Setup & Configuration

1. **Clone this repo.**
2. **Create a `.env` file in the root:**
   ```
   NEWS_API_KEY=your_newsapi_key_here
   ```
3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
4. **Start services:**
   ```
   docker compose up
   ```
5. **Run the producer and consumer:**
   ```
   python3 news_producer.py
   python3 consumer.py
   ```
6. **Start the dashboard:**
   ```
   streamlit run dashboard.py
   ```

## Project Structure
- `news_producer.py`: Fetches news headlines and sends to Kafka (reads API key from `.env`)
- `consumer.py`: Reads messages from Kafka, stores in MongoDB, performs analytics
- `dashboard.py`: Streamlit dashboard for real-time analytics
- `docker-compose.yml`: Runs Kafka, Zookeeper, and MongoDB locally
- `requirements.txt`: Python dependencies
- `.env.example`: Example environment variables (no secrets)
- `screenshots/`: Dashboard images (add your own!)

## Dashboard Screenshot

![Dashboard](screenshots/dashboard.png)

## Security
- **Never commit your `.env` file or API keys to a public repo.**
- Add `.env` to your `.gitignore` to keep secrets safe.

## Credits
- Built with Python, Kafka, MongoDB, Streamlit, NewsAPI, and Docker Compose.

---

Feel free to extend this project with more analytics, visualizations, or data sources!

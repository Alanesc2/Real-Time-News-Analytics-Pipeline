# 🚨 **Real-Time News Analytics Pipeline** (Kafka, MongoDB, Streamlit)

<div align="center">
  <img width="735" alt="Real-time News Analytics" src="https://github.com/user-attachments/assets/5c7c4d16-5001-4005-905d-808db10124fb" />
</div>

<div align="center">
  <img width="735" alt="Streamlit Dashboard" src="https://github.com/user-attachments/assets/f415111e-4e2b-4d35-b15c-1b6770b7852d" />
</div>

This project ingests live **news headlines** from NewsAPI, streams them through **Kafka**, stores them in **MongoDB**, and provides **real-time analytics** on a **Streamlit dashboard**.

## 🚀 **Features**
- 📰 **Real-time News Ingestion** using NewsAPI
- ⚡ **Kafka-based Message Brokering** for scalable data streaming
- 🗃️ **MongoDB Storage** for news data
- 🔑 **Keyword Analytics** on live data
- 📊 **Live Dashboard** powered by Streamlit
- 🐳 **Docker Compose** for easy local development setup
- 🔒 **Environment Variable Support** via `.env` file

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

## 🗂️Project Structure
- `news_producer.py`: Fetches news headlines and sends to Kafka (reads API key from `.env`)
- `consumer.py`: Reads messages from Kafka, stores in MongoDB, performs analytics
- `dashboard.py`: Streamlit dashboard for real-time analytics
- `docker-compose.yml`: Runs Kafka, Zookeeper, and MongoDB locally
- `requirements.txt`: Python dependencies
- `.env.example`: Example environment variables (no secrets)
- `screenshots/`: Dashboard images (add your own!)

## Security
- **Never commit your `.env` file or API keys to a public repo.**
- Add `.env` to your `.gitignore` to keep secrets safe.

## 🌟Credits
- Built with Python, Kafka, MongoDB, Streamlit, NewsAPI, and Docker Compose.

---

Feel free to extend this project with more analytics, visualizations, or data sources!

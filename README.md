# Distributed Streaming System with Python and Kafka

This project demonstrates a simple distributed streaming data pipeline using Python and Apache Kafka. It includes a producer that sends messages to a Kafka topic and a consumer that processes those messages in real time.

## Features
- Python-based Kafka producer and consumer
- Local Kafka setup (via Docker Compose)
- Easy to extend for real-world data sources or sinks

## Getting Started
1. Set up Python environment
2. Start Kafka (recommended: Docker Compose)
3. Run the producer and consumer scripts

## Requirements
- Python 3.8+
- Docker (for local Kafka)
- See `requirements.txt` for Python dependencies

## Project Structure
- `producer.py`: Sends messages to Kafka
- `consumer.py`: Reads and processes messages from Kafka
- `docker-compose.yml`: (Optional) For running Kafka locally

---

Feel free to extend this project with real data sources, additional processing, or database integration!

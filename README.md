# Mobile Money Fraud Detection - Real-Time Data Pipeline

A production-ready real-time data engineering pipeline that simulates mobile money transactions and detects fraudulent behavior using distributed systems, big data tools, and machine learning.

[![License](https://img.shields.io/github/license/Alphadavethedon/Mobile-Money-Fraud-Detection-Real-Time-Data-Pipeline)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Alphadavethedon/Mobile-Money-Fraud-Detection-Real-Time-Data-Pipeline)](https://github.com/Alphadavethedon/Mobile-Money-Fraud-Detection-Real-Time-Data-Pipeline/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Alphadavethedon/Mobile-Money-Fraud-Detection-Real-Time-Data-Pipeline)](https://github.com/Alphadavethedon/Mobile-Money-Fraud-Detection-Real-Time-Data-Pipeline/commits/main)

---

## Overview

This project simulates a mobile money transaction environment to build a **real-time fraud detection pipeline** using open-source technologies and a scalable architecture. It focuses on processing massive streaming data, performing ETL operations, detecting anomalies, and producing real-time alerts.

---

## Architecture

```
+-------------+        +------------+        +-------------+        +-------------+        +-----------+
| Transaction | -----> | Kafka      | -----> | Spark       | -----> | MongoDB     | -----> | Grafana   |
| Simulator   |        | (Stream)   |        | Structured  |        | (Storage)   |        | (Alerts)  |
+-------------+        +------------+        +-------------+        +-------------+        +-----------+
                                             | ML Model |
```

---

## Features

- Stream ingestion using **Apache Kafka**
- Real-time processing with **Apache Spark Structured Streaming**
- Feature engineering and prediction using **Scikit-learn**
- Transaction storage in **MongoDB**
- Real-time dashboards with **Grafana**
- Containerized using **Docker** and orchestrated with **Docker Compose**

---

## Tech Stack

| Category              | Technologies                                                                 |
|-----------------------|-------------------------------------------------------------------------------|
| Programming Languages | Python, Bash                                                                 |
| Data Ingestion        | Kafka, Faker                                                                 |
| Stream Processing     | Apache Spark Structured Streaming                                            |
| Machine Learning      | Scikit-learn                                                                 |
| Storage               | MongoDB                                                                      |
| Monitoring & Alerts   | Prometheus, Grafana                                                           |
| Containerization      | Docker, Docker Compose                                                        |
| Orchestration         | Shell Scripts, systemd (or Kubernetes-ready)                                 |

---

## Setup & Usage

### Prerequisites

- Docker + Docker Compose
- Python 3.8+
- Make / Shell

### Quickstart

```bash
# Clone the repo
git clone https://github.com/Alphadavethedon/Mobile-Money-Fraud-Detection-Real-Time-Data-Pipeline.git
cd Mobile-Money-Fraud-Detection-Real-Time-Data-Pipeline

# Start the full pipeline
docker-compose up --build
```

---

## Project Structure

```
├── data-simulator/         # Python-based transaction generator
├── kafka/                  # Kafka & Zookeeper config
├── spark/                  # Spark stream processor with ML model
├── models/                 # Trained fraud detection model
├── monitoring/             # Prometheus & Grafana dashboards
├── docker-compose.yml      # Service orchestration
└── README.md
```

---

## Real-Time Dashboard

> Live transaction and fraud detection monitoring powered by Grafana.

![Dashboard Screenshot](https://github.com/Alphadavethedon/Mobile-Money-Fraud-Detection-Real-Time-Data-Pipeline/blob/main/docs/grafana-dashboard.png)

---

## Model Performance

- Accuracy: `95.4%`
- Precision: `91.2%`
- Recall: `93.5%`
- F1-Score: `92.3%`

Trained on real-world mobile money transaction datasets (publicly available on [Kaggle](https://www.kaggle.com/datasets/ntnu-testimon/paysim1))

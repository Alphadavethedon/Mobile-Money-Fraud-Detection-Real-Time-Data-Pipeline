# Mobile Money Fraud Detection & Real-Time Data Pipeline

## Overview

A real-time data engineering project simulating mobile money (e.g., M-Pesa) transactions to detect fraud using a modern data stack. This end-to-end pipeline showcases real-time ingestion, stream processing, feature engineering, fraud detection, alerting, and interactive dashboards.

Built for aspiring Data Engineers & ML Engineers looking to demonstrate real-world impact and land jobs in the FinTech, Banking, or Telco sectors.

---

## 🚀 Features
- Real-time data ingestion from simulated M-Pesa-like APIs
- Stream processing with Apache Kafka and Spark Structured Streaming
- Feature engineering & windowed aggregations for user behavior
- Fraud detection using basic rules & ML classifiers
- Alerting & logging suspicious transactions
- Dashboarding with Streamlit & Power BI
- CI/CD-ready with Docker & GitHub Actions
- Cloud-friendly (deployable on AWS/GCP/Azure)

---

## 🛠️ Tech Stack

### 🧪 Data Simulation
- Python
- Faker

### 📨 Ingestion
- Kafka  
- Kafka Connect

### 🔄 Stream Processing
- Apache Spark
- PySpark
- Spark Structured Streaming

### 🧹 ETL & Orchestration
- Apache Airflow
- dbt (optional)

### 🧠 Fraud Detection (ML/Rules-Based)
- Scikit-learn / XGBoost
- Pandas
- Featuretools

### 🗄️ Storage
- PostgreSQL
- Amazon S3 / MinIO

### 📊 Dashboards
- Streamlit  
- Power BI or Superset

### 🔒 Security (Optional)
- HashiCorp Vault (for storing secrets)

### ⚙️ DevOps & Deployment
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- AWS EC2 / GCP Compute Engine / Render

---

## 🧱 Project Structure
```
mobile-money-fraud-pipeline/
│
├── data_generator/              # Python-based data simulation (M-Pesa style)
├── kafka/                      # Kafka + Zookeeper + Connect setup
├── spark_jobs/                # Real-time processing scripts using PySpark
├── airflow/                   # DAGs for batch jobs / ML retraining
├── models/                    # ML model training and serialized models
├── dashboard/                 # Streamlit app or PowerBI dashboards
├── docker-compose.yml         # All services wired together
└── README.md
```

---

## 📦 How to Run

```bash
# Clone the repo
$ git clone https://github.com/yourusername/mobile-money-fraud-pipeline.git
$ cd mobile-money-fraud-pipeline

# Start all services (Kafka, Spark, etc.)
$ docker-compose up --build

# Open Streamlit dashboard
$ streamlit run dashboard/app.py
```

---

## 🌍 Real-World Use Cases
- Mobile money fraud detection (e.g., M-Pesa, Airtel Money, T-Kash)
- Behavioral analytics for financial transactions
- Event-driven architectures in FinTech
- Stream processing jobs for real-time alerts

---

## 🎯 Who This Is For
- Aspiring Data Engineers
- Junior/Mid Backend Engineers exploring data streams
- FinTech candidates targeting KCB, Tala, Branch, Equity, Absa, Safaricom, Cellulant, etc.

---

## 📚 Resources & Inspiration
- [Kafka for Data Engineers](https://www.confluent.io/learn)
- [Spark Structured Streaming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Airflow Quick Start](https://airflow.apache.org/docs/apache-airflow/stable/start/index.html)

---

## 📫 Contact
**Davis Wabwile**  
Fullstack Engineer | DevOps | Cloud | AI/ML | Data  
📧 davewabwile@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/daviswabwile)  
🌐 [Portfolio](https://alphadavethedon.github.io/Davis-portfolio)  
📝 [Medium Blog](https://medium.com/@daviswabwile)

---




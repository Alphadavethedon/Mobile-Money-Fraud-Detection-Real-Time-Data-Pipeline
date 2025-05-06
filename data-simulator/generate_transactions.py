# data-simulator/generate_transactions.py

import pandas as pd
import numpy as np
from faker import Faker
import random
import time
import json

fake = Faker()

def generate_transaction():
    return {
        "transaction_id": fake.uuid4(),
        "timestamp": fake.iso8601(),
        "sender": fake.phone_number(),
        "receiver": fake.phone_number(),
        "amount": round(random.uniform(10, 10000), 2),
        "transaction_type": random.choice(["withdrawal", "deposit", "payment", "transfer"]),
        "location": fake.city(),
        "device_id": fake.uuid4(),
        "is_fraud": np.random.choice([0, 1], p=[0.98, 0.02])  # 2% fraud rate
    }

if __name__ == "__main__":
    while True:
        transaction = generate_transaction()
        print(json.dumps(transaction))  # This would go to Kafka in future
        time.sleep(1)

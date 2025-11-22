from pathlib import Path
import pandas as pd
import random
import uuid
import time

DATA_DIR = Path(__file__).parent / "data"

# Load dataframes once
names = pd.read_csv(DATA_DIR / "names_extended.csv")
cities = pd.read_csv(DATA_DIR / "cities_extended.csv")
merchants = pd.read_csv(DATA_DIR / "merchants_extended.csv")
addresses = pd.read_csv(DATA_DIR / "addresses_extended.csv")

# Clean column names
for df in (names, cities, merchants, addresses):
    df.columns = df.columns.str.strip()


def build_transaction():
    """Construct a single synthetic transaction event.

    Returns a plain Python dict suitable for encoding or JSON serialisation.
    """
    user = names.sample(1).iloc[0]
    city = cities.sample(1).iloc[0]["city"]
    merchant = merchants.sample(1).iloc[0]

    return {
        "transaction_id": str(uuid.uuid4()),
        "user_id": str(uuid.uuid4()),
        "amount": round(random.uniform(10, 5000), 2),
        "currency": "USD",
        "merchant_name": merchant["merchant"],
        "merchant_category": merchant["category"],
        "transaction_type": random.choice(["purchase", "refund", "transfer", "withdrawal"]),
        "timestamp": int(time.time() * 1000),
        "device_id": str(uuid.uuid4()),
        "location": city,
        "status": random.choice(["completed", "pending", "failed"])
    }


def generate_transactions(count=1):
    """Generate multiple transaction records."""
    return [build_transaction() for _ in range(count)]

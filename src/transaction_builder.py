import random
import uuid
import time

def build_transaction(names, cities, merchants, addresses):
    """Construct a single synthetic transaction event."""

    user = names.sample(1).iloc[0]
    city = cities.sample(1).iloc[0]["city"]
    addr = addresses.sample(1).iloc[0]["address"]
    merchant = merchants.sample(1).iloc[0]

    transaction = {
        "transaction_id": str(uuid.uuid4()),
        "user_name": user["name"],
        "email": user["email"],
        "phone": user["phone"],

        "merchant": merchant["merchant"],
        "category": merchant["category"],

        "amount": round(random.uniform(99, 9999), 2),
        "timestamp": int(time.time() * 1000),

        "city": city,
        "address": addr,
    }

    return transaction
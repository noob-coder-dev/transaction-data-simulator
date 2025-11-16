from confluent_kafka import Producer, Consumer, KafkaException


def create_producer(bootstrap_servers="localhost:9092"):
    config = {
        "bootstrap.servers": bootstrap_servers,
        "acks": "all",
        "compression.type": "lz4",
    }
    return Producer(config)


def send_message(producer, topic, key, value):
    try:
        producer.produce(topic, key=key, value=value)
        producer.flush()
    except KafkaException as e:
        print(f"Kafka send error: {e}")


def create_consumer(
    topic,
    group_id="transaction-validator",
    bootstrap_servers="localhost:9092"
):
    config = {
        "bootstrap.servers": bootstrap_servers,
        "group.id": group_id,
        "auto.offset.reset": "earliest"
    }

    consumer = Consumer(config)
    consumer.subscribe([topic])
    return consumer


def consume_messages(consumer, max_messages=10):
    """Fetch up to N messages."""
    messages = []
    while len(messages) < max_messages:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print("Kafka error:", msg.error())
            continue
        messages.append(msg)
    return messages
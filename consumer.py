from kafka import KafkaConsumer
import json


if __name__ == "__main__":
    consumer = KafkaConsumer(
        "user_details",
        bootstrap_servers="<ip>:9092",
        auto_offset_reset="earliest",
        group_id="consumer-group-1")
    print("Starting the consumer")
    for msg in consumer:
        print("User Details: {}".format(json.loads(msg.value)))

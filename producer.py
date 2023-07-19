from kafka import KafkaProducer
import json
from data import get_random_user_details
import time


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


def get_partition(key, all, available):
    return 0

producer = KafkaProducer(bootstrap_servers=['10.104.117.91'], value_serializer=json_serializer) #partitioner=get_partition


if __name__ == "__main__":
    while True:
        ran_user = get_random_user_details()
        print(ran_user)
        # provide topic name and data
        producer.send("user_details", ran_user)
        time.sleep(5)


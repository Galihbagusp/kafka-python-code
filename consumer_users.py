import json
from kafka import KafkaConsumer
import pandas as pd

if __name__ == '__main__':
    # Kafka Consumer
    consumer = KafkaConsumer(
        'users',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest'
    )
    for message in consumer:
        json_file = json.loads(message.value)
        print(json_file)
        df = pd.DataFrame.from_records([json_file])
        df.to_csv(
            '/home/galihbaguspr/kafka-python-code/output/consumer_users.csv')

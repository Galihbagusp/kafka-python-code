from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import csv
from time import sleep
import re

def load_avro_schema_from_file():
    key_schema = avro.load(
        "/home/galihbaguspr/kafka-python-code/bitcoin_bigquery/bitcoin_price_key.avsc")
    value_schema = avro.load(
        "/home/galihbaguspr/kafka-python-code/bitcoin_bigquery/bitcoin_price_value.avsc")

    return key_schema, value_schema


def send_record():
    key_schema, value_schema = load_avro_schema_from_file()

    producer_config = {
        "bootstrap.servers": "localhost:9092",
        "schema.registry.url": "http://localhost:8081",
        "acks": "1"
    }

    producer = AvroProducer(producer_config, default_key_schema=key_schema, default_value_schema=value_schema)

    file = open(
        '/home/galihbaguspr/kafka-python-code/bitcoin_bigquery/data/bitcoin_price_Training.csv')
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        key = {"Date":  str(row[0])}
        value = {"Date": str(row[0]), "Open": float(row[1]), "High": float(row[2]), "Low": float(row[3]), "Close": float(row[4]), "Volume": str(row[5]), "MarketCap": str(row[6])}

        try:
            producer.produce(topic='practice.bitcoin_price_Training', key=key, value=value)
        except Exception as e:
            print(f"Exception while producing record value - {value}: {e}")
        else:
            print(f"Successfully producing record value - {value}")

        producer.flush()
        sleep(1)

if __name__ == "__main__":
    send_record()

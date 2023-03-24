from confluent_kafka import Consumer

def read_messages():
    consumer_config = {"bootstrap.servers": "localhost:9092",
                       "group.id": "users",
                       "enable.auto.commit": False,
                       "auto.offset.reset": "earliest"}

    consumer = Consumer(consumer_config)
    consumer.subscribe(["users"])

    while(True):
        try:
            message = consumer.poll(10)
        except Exception as e:
            print(f"Exception while trying to poll messages - {e}")
        else:
            if message:
                print(f"Successfully poll a record from "
                      f"Kafka topic: {message.topic()}, partition: {message.partition()}, offset: {message.offset()}\n"
                      f"message key: {message.key()} || message value: {message.value()}")
                
    consumer.close()


if __name__ == "__main__":
    read_messages()


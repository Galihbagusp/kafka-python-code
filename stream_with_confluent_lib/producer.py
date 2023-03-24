import json
from csv import DictReader
from datetime import datetime
from confluent_kafka import Producer
from time import sleep

conf = {'bootstrap.servers':'localhost:9092'}
producer = Producer(conf)
topic = 'users'

if __name__ == '__main__':
    with open('/home/galihbaguspr/kafka-python-code/stream_with_confluent_lib/bank-additional-full.csv','r') as item:
        csv_reader = DictReader(item,delimiter=';')
        for row in csv_reader:
            try:
                producer.poll(10)
                snd = producer.produce('users', json.dumps(row).encode('utf-8'),
                                   callback = lambda err, msg: print(f'Producing Message @ {datetime.now()} | Message Delivered to Topic =>', msg.topic()))
            except BufferError as bfer:
                print('BufferError:{}'.format(bfer))
            producer.flush()
            sleep(1)
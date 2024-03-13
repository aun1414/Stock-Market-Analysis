from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json

consumer = KafkaConsumer(
    'demo_testing2',
     bootstrap_servers=['3.94.116.179:9092'], 
    value_deserializer=lambda x: loads(x.decode('utf-8')))

s3 = S3FileSystem()
for count, i in enumerate(consumer):
    with s3.open("s3://kafka-stock-market-tutorial-youtube-darshil/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file)    
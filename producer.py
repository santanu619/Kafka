from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0,10,1))
now = datetime.now()
current_time = now.strftime('%d/%m/%Y %H/%M/%S')

producer.send('kafkaDemo', b'Starting Producer')
for i in range(100):
    message = "Message {} {}".format((i + 1), str(datetime.now().time()))
    producer.send('kafkaDemo', json.dumps(message).encode('utf-8'))
    sleep(2)

    print('message sent',(i+1))
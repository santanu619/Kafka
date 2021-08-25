from kafka import KafkaConsumer

consumer = KafkaConsumer('kafkaDemo',bootstrap_servers=['localhost:9092'], api_version=(0,10,1))
for msg in consumer:
    print (msg.value)
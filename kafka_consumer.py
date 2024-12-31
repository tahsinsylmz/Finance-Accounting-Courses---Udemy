from kafka import KafkaConsumer
import json

# Kafka Consumer
consumer = KafkaConsumer('anomalies', bootstrap_servers='localhost:9092', value_deserializer=lambda x: json.loads(x.decode('utf-8')))
print("Mesajlar dinleniyor...")
with open("anomalies_log.txt", "a") as f:
    for message in consumer:
        print(message.value)
        f.write(f"{message.value}\n")

from kafka import KafkaProducer
import json

# Kafka Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: json.dumps(x).encode('utf-8'))
producer.send('anomalies', value={"price": 100, "subscribers": 1000, "status": "Anomaly"})
print("Mesaj gönderildi.")

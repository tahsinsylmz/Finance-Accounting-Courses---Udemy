from pyspark.sql import SparkSession
from pyspark.streaming.kafka import KafkaUtils
from pyspark.ml.feature import StandardScaler
from pyspark.ml.clustering import KMeans
from pyspark.sql.types import StructType, StructField, FloatType, StringType

# Spark Session
spark = SparkSession.builder.appName("RealTimeAnomalyDetection").getOrCreate()

# Kafka’dan veri çekme
lines = KafkaUtils.createStream(spark, "localhost:9092", "spark-streaming", {"anomalies": 1})

# Veri şeması tanımlama
schema = StructType([
    StructField("price", FloatType(), True),
    StructField("subscribers", FloatType(), True),
    StructField("status", StringType(), True)
])

# Anomali Tespiti
df = spark.readStream.schema(schema).json(lines)
scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures")
kmeans = KMeans(k=2, seed=1).fit(df)
print("Anomali tespiti tamamlandı.")

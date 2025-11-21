from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

bronze_path = "/mnt/raw/bronze/source_data"
bronze_delta_path = "/mnt/delta/bronze"

df = spark.read.format("csv").option("header", True).load(bronze_path)

df.write.format("delta").mode("overwrite").save(bronze_delta_path)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

bronze_delta_path = "/mnt/delta/bronze"
silver_delta_path = "/mnt/delta/silver"

df_bronze = spark.read.format("delta").load(bronze_delta_path)

df_silver = df_bronze.dropDuplicates()

df_silver.write.format("delta").mode("overwrite").save(silver_delta_path)

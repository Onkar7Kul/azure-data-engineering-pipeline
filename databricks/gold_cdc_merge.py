from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

silver_delta_path = "/mnt/delta/silver"
gold_delta_path = "/mnt/delta/gold"

df_new = spark.read.format("delta").load(silver_delta_path)
df_gold = spark.read.format("delta").load(gold_delta_path)

(df_gold.alias("t")
 .merge(
     df_new.alias("s"),
     "t.id = s.id"
 )
 .whenMatchedUpdateAll()
 .whenNotMatchedInsertAll()
 .execute()
)

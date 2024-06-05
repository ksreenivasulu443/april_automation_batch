import json

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col

# Initialize a Spark session
spark = SparkSession.builder.appName("CarTable").getOrCreate()

with open(r"D:\ETL_Automation\ReadFiles\multiple_arry.json") as data_file:
    data = json.load(data_file)
# Convert the JSON data to an RDD
rdd = spark.sparkContext.parallelize([data])

# Convert the RDD to a DataFrame
df = spark.read.json(rdd)

# Explode the cars dictionary into rows
df = df.select(explode(col("cars")).alias("brand", "details"))

# Explode the details array into rows
df = df.select(col("brand"), explode(col("details")).alias("detail"))

# Select the necessary columns and display the result
result_df = df.select(col("brand"), col("detail.model").alias("model"), col("detail.doors").alias("doors"))
result_df.show()

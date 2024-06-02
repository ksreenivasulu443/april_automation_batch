from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("dataframe").getOrCreate()

df = spark.read.option("header", True).csv("/Users/harish/PycharmProjects/april_automation_batch/FIles2/test_files/*.csv")

df.show()

print(df.count())
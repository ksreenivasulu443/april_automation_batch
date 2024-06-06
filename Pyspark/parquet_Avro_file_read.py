# Databricks notebook source
df = spark.read.parquet("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/parquet/userdata1.parquet")

df.display()

df.printSchema()

# df = spark.read.format('parquet').load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/parquet/userdata1.parquet")


# COMMAND ----------


df = spark.read.format("avro").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/userdata1.avro")

df.printSchema()

df.display()

# COMMAND ----------



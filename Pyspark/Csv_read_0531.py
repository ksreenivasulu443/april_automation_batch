# Databricks notebook source

df1 = spark.read.format("csv").option("header", "true").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/IPL_Ball_by_Ball_2008_2020.csv")

df1.display()

# COMMAND ----------

df1.printSchema()

# COMMAND ----------

help(spark.read)

# COMMAND ----------

df1 = spark.read.format("csv").option("header", "true").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/IPL_Matches_2008_2020-2.csv")

df1.display()

from pyspark.sql.functions import spark_partition_id, asc, desc
df1\
    .withColumn("partitionId", spark_partition_id()) \
    .groupBy("partitionId")\
    .count()\
    .orderBy(asc("count"))\
    .show()

# COMMAND ----------

df1.printSchema()

# COMMAND ----------

print(df1.count())

len(df1.columns)

# COMMAND ----------

print(df1.rdd.getNumPartitions())

# COMMAND ----------

df1 = df1.repartition(10)

# COMMAND ----------

df.show()

# COMMAND ----------

df1 = spark.read.format("csv").option("header", "true").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/april_batch2/Contact_info_t.csv")
df2 = spark.read.format("csv").option("header", "true").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/april_batch2/Contact_info.csv")

print(df1.count())
print(df2.count())
final_data = df1.unionAll(df2)
print(final_data.count())

final_dataset2 = spark.read.format("csv").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/april_batch2/*20240531*.csv")



print(final_dataset2.count())

# COMMAND ----------

final_dataset2.display()

# COMMAND ----------



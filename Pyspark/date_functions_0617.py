# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    current_date, current_timestamp, year, month, dayofmonth, hour,
    date_add, date_sub, datediff, add_months, months_between,
    date_format, to_date, to_timestamp, quarter,lit,col
)

# Sample data
data = [(1,"2023-01-01", "2023-01-08 12:34:56"), (2,"2023-06-01", "2023-06-08 23:45:01"), (3,"2023-12-31", "2024-01-01 00:00:00")]
columns = ["id","date_column", "timestamp_column"]

# Create DataFrame
df = spark.createDataFrame(data, columns)
df.show()
df.printSchema()

# Apply date functions



# COMMAND ----------

df1 = df.select(
    "id",
    "date_column",
    "timestamp_column",
    current_date().alias("current_date"),
    current_timestamp().alias("current_timestamp"),
    year(current_date()).alias("year"),
    month("date_column").alias("month"),
    quarter("date_column").alias("quarter"),
    quarter(current_date()).alias("current_quarter"),
    dayofmonth(current_date()).alias("day_of_month"),
    hour("timestamp_column").alias("hour"),
    date_add("date_column", 7).alias("date_plus_7"),
    date_sub("date_column", 7).alias("date_minus_7"),
    datediff("timestamp_column", "date_column").alias("datediff_days"),
    add_months("date_column", 1).alias("next_month"),
    months_between("timestamp_column", "date_column").alias("months_between"),
    date_format("date_column", "yyyy/MMM/d").alias("formatted_date"),
    to_date("timestamp_column", "yyyy-MM-dd HH:mm:ss").alias("to_date"),
    to_timestamp("date_column", "yyyy-MM-dd").alias("to_timestamp")
).filter('month=6')

# Show results
df1.display()

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    current_date, current_timestamp, year, month, dayofmonth, hour,
    date_add, date_sub, datediff, add_months, months_between,
    date_format, to_date, to_timestamp
)

# Sample data
data = [(1,"2023-01-01", "2023-01-08 12:34:56"), (2,"2023-06-01", "2023-06-08 23:45:01"), (3,"2023-12-31", "2024-01-01 00:00:00")]
columns = ["id","date_column", "timestamp_column"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Apply date functions using withColumn to a single DataFrame
df = df.withColumn("current_date", current_date()) \
       .withColumn("current_timestamp", current_timestamp()) \
       .withColumn("year", year("date_column")) \
       .withColumn("month", month("date_column")) \
       .withColumn("day_of_month", dayofmonth("date_column")) \
       .withColumn("hour", hour("timestamp_column")) \
       .withColumn("date_plus_7", date_add("date_column", 7)) \
       .withColumn("date_minus_7", date_sub("date_column", 7)) \
       .withColumn("datediff_days", datediff("timestamp_column", "date_column")) \
       .withColumn("next_month", add_months("date_column", 1)) \
       .withColumn("months_between", months_between("timestamp_column", "date_column")) \
       .withColumn("formatted_date", date_format("date_column", "yyyy/MM/dd")) \
       .withColumn("to_date", to_date("timestamp_column", "yyyy-MM-dd HH:mm:ss")) \
       .withColumn("to_timestamp", to_timestamp("date_column", "yyyy-MM-dd")) \
       .withColumn("id2", lit(2)*col('id')).where(' year=2023 ')

# Show results
df.display()


# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Initialize Spark session
spark = SparkSession.builder.appName("DateFunctionsExample").getOrCreate()

# Sample data
data = [("2023-01-01", "2023-01-08 12:34:56"), ("2023-06-01", "2023-06-08 23:45:01"), ("2023-12-31", "2024-01-01 00:00:00")]
columns = ["date_column", "timestamp_column"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Create a temporary view
df.createOrReplaceTempView("dates_table")

# SQL query to apply date functions



# Execute the query
result_df = spark.sql("""SELECT
    date_column,
    timestamp_column,
    current_date() AS current_date,
    current_timestamp() AS current_timestamp,
    year(date_column) AS year,
    month(date_column) AS month,
    dayofmonth(date_column) AS day_of_month,
    hour(timestamp_column) AS hour,
    date_add(date_column, 7) AS date_plus_7,
    date_sub(date_column, 7) AS date_minus_7,
    datediff(timestamp_column, date_column) AS datediff_days,
    add_months(date_column, 1) AS next_month,
    months_between(timestamp_column, date_column) AS months_between,
    date_format(date_column, 'yyyy/MM/dd') AS formatted_date,
    to_date(timestamp_column, 'yyyy-MM-dd HH:mm:ss') AS to_date,
    to_timestamp(date_column, 'yyyy-MM-dd') AS to_timestamp
FROM dates_table
""")

# Show results
result_df.display()


# COMMAND ----------



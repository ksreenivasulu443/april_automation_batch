# Databricks notebook source
# jdbc_url = 'jdbc:snowflake://oborokf-kh65378.snowflakecomputing.com/?user=KSREENIVASULU&password=Dharmavaram1@&warehouse=COMPUTE_WH&db=SAMPLE&schema=CONTACT_INFO'

df = spark.read \
    .format("jdbc") \
    .option("driver", "net.snowflake.client.jdbc.SnowflakeDriver") \
    .option("url", 'jdbc:snowflake://oborokf-kh65378.snowflakecomputing.com/?user=KSREENIVASULU&password=Dharmavaram1@&warehouse=COMPUTE_WH&db=SAMPLE&schema=CONTACT_INFO') \
    .option("query", 'select identifier from CONTACT_INFO_RAW')     \
    .load()

1. create snowflake account
2. download and install postgres db
3. download and install oracle db
4. Azure sqlserver db

# COMMAND ----------

df.display()

# COMMAND ----------



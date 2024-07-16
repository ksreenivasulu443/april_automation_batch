import spark.sql

jdbc_url = 'jdbc:snowflake://oborokf-kh65378.snowflakecomputing.com/?user=KSREENIVASULU&password=Dharmavaram1@&warehouse=COMPUTE_WH&db=SAMPLE&schema=CONTACT_INFO'

df = spark.read \
    .format("jdbc") \
    .option("driver", "net.snowflake.client.jdbc.SnowflakeDriver") \
    .option("url", jdbc_url) \
    .option("dbtable", 'CONTACT_INFO_RAW') \
    .load()

df.show()

from pyspark.sql import SparkSession

jar_path = '/Users/harish/PycharmProjects/april_automation_batch/jars/snowflake-jdbc-3.14.3.jar'
# Create SparkSession
spark = SparkSession.builder.master("local[2]") \
    .appName("test") \
    .config("spark.jars", '/Users/harish/PycharmProjects/april_automation_batch/jars/snowflake-jdbc-3.14.3.jar') \
    .config("spark.driver.extraClassPath", '/Users/harish/PycharmProjects/april_automation_batch/jars/snowflake-jdbc-3.14.3.jar') \
    .config("spark.executor.extraClassPath", '/Users/harish/PycharmProjects/april_automation_batch/jars/snowflake-jdbc-3.14.3.jar') \
    .getOrCreate()

jdbc_url = 'jdbc:snowflake://oborokf-kh65378.snowflakecomputing.com/?user=KSREENIVASULU&password=Dharmavaram1@&warehouse=COMPUTE_WH&db=SAMPLE&schema=CONTACT_INFO'

df = spark.read \
    .format("jdbc") \
    .option("driver", "net.snowflake.client.jdbc.SnowflakeDriver") \
    .option("url", jdbc_url) \
    .option("dbtable", 'CONTACT_INFO_RAW')     \
    .load()


df.show()


from pyspark.sql import SparkSession

jar_path = r'C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\snowflake-jdbc-3.14.3.jar'
# Create SparkSession
spark = SparkSession.builder.master("local") \
    .appName("test") \
    .config("spark.jars", r'C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\snowflake-jdbc-3.14.3.jar') \
    .config("spark.driver.extraClassPath", r'C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\snowflake-jdbc-3.14.3.jar') \
    .config("spark.executor.extraClassPath", r'C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\snowflake-jdbc-3.14.3.jar') \
    .getOrCreate()

jdbc_url = 'jdbc:snowflake://fxfnlzv-zr16398.snowflakecomputing.com/?user=AJAY&password=Snowflake5@sql&warehouse=COMPUTE_WH&db=MYDB&schema=DBO'

df = spark.read \
    .format("jdbc") \
    .option("driver", "net.snowflake.client.jdbc.SnowflakeDriver") \
    .option("url", jdbc_url) \
    .option("query", 'select * from CONTACT_INFO')     \
    .load()
# .option("dbtable", 'CONTACT_INFO')     \

df.show()

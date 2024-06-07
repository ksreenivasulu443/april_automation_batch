
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[2]") \
    .appName("test") \
    .config("spark.jars", '/Users/harish/PycharmProjects/april_automation_batch/jars/postgresql-42.2.5.jar') \
    .config("spark.driver.extraClassPath", '/Users/harish/PycharmProjects/april_automation_batch/jars/postgresql-42.2.5.jar') \
    .config("spark.executor.extraClassPath", '/Users/harish/PycharmProjects/april_automation_batch/jars/postgresql-42.2.5.jar') \
    .getOrCreate()

df2 = spark.read.format("jdbc"). \
    option("url", "jdbc:postgresql://localhost:5432/postgres"). \
    option("user", "postgres"). \
    option("password", "Dharmavaram1@"). \
    option("query", "select * from contact_info_raw"). \
    option("driver", "org.postgresql.Driver").load()

df2.show()

df2 = spark.read.format("jdbc"). \
    option("url", "jdbc:oracle:thin:@//localhost:1521/freepdb1"). \
    option("user", "scott"). \
    option("password", "tiger"). \
    option("query", "select * from contact_info_raw"). \
    option("driver", "org.postgresql.Driver").load()

df2.show()









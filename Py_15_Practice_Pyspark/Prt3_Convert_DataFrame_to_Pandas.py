from pyspark.sql import SparkSession
import pandas as pd


# Create a Spark session
spark = SparkSession.builder \
    .appName("PySpark to Pandas Example") \
    .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
    .getOrCreate()

# Create a sample PySpark DataFrame
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
columns = ["Name", "Id"]
spark_df = spark.createDataFrame(data, columns)

# Convert the PySpark DataFrame to a Pandas DataFrame
pandas_df = spark_df.toPandas()

# Print the Pandas DataFrame
# print(pandas_df)


pd.DataFrame(pandas_df).show()
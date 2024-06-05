from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local').appName('DataFrame').getOrCreate()
# spark = SparkSession.builder.master('local[1]').appName('DataFrame').getOrCreate()

dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
df = spark.createDataFrame(dataList, schema=['Language', 'fee'])

# df.show() # All rows will display in output

df.show(n=2)  # Only 2 rows will display in output

df.show(n=2, truncate=5)  # truncate will display number of character in output

spark.stop()

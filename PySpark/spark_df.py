from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.master("local[1]").appName("dataframe").getOrCreate()
dataList = [("Java", 20000), ("Python - pyspark - dataframe", 100000), ("Scala", 3000)]
df=spark.createDataFrame(dataList, schema=['Language','fee'])
df.show(n=3,truncate=3)



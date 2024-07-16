from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()
dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
df = spark.createDataFrame(dataList, schema=['Language', 'fee'])

df.show(n=1,truncate=4)

# spark.stop()

# data = [(1,'sreeni',30),(2,'Raghav', 30), (3, 'Hari',50)]
# schema = ['id', 'name', 'age']
# df = spark.createDataFrame(data=data, schema=schema)
# df.show()
# df.printSchema()

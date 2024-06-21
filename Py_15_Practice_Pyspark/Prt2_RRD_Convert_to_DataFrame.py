from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

dept = [("Finance",10),("Marketing",20),("Sales",30),("IT",40)]

# RDD Data Frame
rdd = spark.sparkContext.parallelize(dept)  # RDD accept only Data or rows

#  RDD converting to DATAFRAME method1
df = rdd.toDF(['Dep', 'Depno'])  # DataFrame will accept column also
df.printSchema()
df.show(truncate=False)

#  RDD converting to DATAFRAME method2
df1 = spark.createDataFrame(rdd, ['Dep', 'Depno'])

df1.show()


# DATAFRAME converting to RDD
df2 = df1.rdd

print(df2.collect())


spark.stop()
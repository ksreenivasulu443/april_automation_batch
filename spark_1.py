from pyspark.sql import SparkSession

data = [(1,2)]
schema = ['col1','col2']
spark = SparkSession.builder.getOrCreate()
spark.createDataFrame(data=data, schema=schema).show()
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.master("local[1]").appName("dataframe").getOrCreate()
dataList = [("Java", 20000), ("Python - pyspark - dataframe", 100000), ("Scala", 3000)]
df=spark.createDataFrame(dataList, schema=['Language','fee'])
df.show(n=3,truncate=3)

list_of_tuples = [(1,'sreeni',30),(2,'Raghav', 30), (3, 'Hari',50)]
schema_for_list_of_tuple = ['id', 'name', 'age']
df = spark.createDataFrame(data=list_of_tuples, schema=schema_for_list_of_tuple)
df.show()
df.printSchema()

data = [(1,'sreeni',30),(2,'Raghav', 30), (3, 'Hari',50)]

schema = 'id integer, name string, age integer'

df = spark.createDataFrame(data=data, schema=schema)

df.show()

df.printSchema()

from pyspark.sql.types import StructField, StructType, StringType, IntegerType,FloatType,LongType, DecimalType

# schema = 'id integer, name string, age integer'
schema=  StructType([StructField('id', LongType(), True),
 StructField('name', StringType(), True),
 StructField('age', IntegerType(), True)])

data = [(1,'sreeni',None),(2,'Raghav', 30), (3, 'Hari',50)]
df3 = spark.createDataFrame(data=data, schema=schema3)
# df3.show()
#df3.display()
display(df3)


spark.stop()

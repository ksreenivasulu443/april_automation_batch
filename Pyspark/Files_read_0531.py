# Databricks notebook source
df1 = spark.read.format("json").option("multiline", True).load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/april_batch2/sample1.json")

# COMMAND ----------

df1.show()

# COMMAND ----------

df1.printSchema()

# COMMAND ----------

df1 = spark.read.format("json").option("multiline", False).load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/april_batch2/singleline.json")

# COMMAND ----------

df1.display()

# COMMAND ----------

df1.printSchema()

# COMMAND ----------

# df1 = spark.read.format("json").option("multiline", "True").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/sample4.json")

# df1 = spark.read.format("json").option("multiline", True).load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/april_batch2/Complex2.json")

df1 = spark.read.format("json").option("multiline", True).load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/april_batch2/Complex2-1.json")

df1.show()

df1.printSchema()

# In pyspark we will have two complex datatypes 1. Array type(explode)--> increase the rows, 2. Structtype(use struct colname.column)

# COMMAND ----------

df1.display()

# COMMAND ----------

from pyspark.sql.functions import explode, explode_outer, upper,lower, instr, lead,lag, substring, length,col

from pyspark.sql.types import *

# COMMAND ----------

df2 = df1.select(explode("people").alias("all_columns"))

# COMMAND ----------

df2.display()

# COMMAND ----------

df2.printSchema()

# COMMAND ----------

df3 = df2.select(df2.all_columns.age.alias("age"), df2.all_columns.firstName.alias("firstname"), df2.all_columns.gender, df2.all_columns.lastName, df2.all_columns.middle,df2.all_columns.number,df2.all_columns.college)

df3.display()

# COMMAND ----------

df5 = spark.read.format("json").option("multiline", "True").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/sample4.json")

df5.display()

# COMMAND ----------

df4 = spark.read.format("json").option("multiline", True).load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/april_batch2/Complex2-1.json")

df4.printSchema()

# COMMAND ----------

from pyspark.sql.functions import explode, explode_outer, upper,lower, instr, lead,lag, substring, length,col

from pyspark.sql.types import *
def flatten(df):
    # compute Complex Fields (Lists and Structs) in Schema
    complex_fields = dict([(field.name, field.dataType)
                           for field in df.schema.fields
                           if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    while len(complex_fields) != 0:
        col_name = list(complex_fields.keys())[0]
        print("Processing :" + col_name + " Type : " + str(type(complex_fields[col_name])))

        # if StructType then convert all sub element to columns.
        # i.e. flatten structs
        if type(complex_fields[col_name]) == StructType:
            expanded = [col(col_name + '.' + k).alias(col_name + '_' + k) for k in
                        [n.name for n in complex_fields[col_name]]]
            df = df.select("*", *expanded).drop(col_name)

        # if ArrayType then add the Array Elements as Rows using the explode function
        # i.e. explode Arrays
        elif type(complex_fields[col_name]) == ArrayType:
            df = df.withColumn(col_name, explode_outer(col_name))

        # recompute remaining Complex Fields in Schema
        complex_fields = dict([(field.name, field.dataType)
                               for field in df.schema.fields
                               if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    return df


# COMMAND ----------

df5 = flatten(df4)

df5.display()

# COMMAND ----------

df6.printSchema()

# COMMAND ----------



# COMMAND ----------

df1 = spark.read.option("multiline", "True").json("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/sample2.json")

df1.display()

# COMMAND ----------

df2 = df1.select("*", explode("phoneNumbers").alias("phone")).drop("phoneNumbers")
df2.printSchema()

# COMMAND ----------

df2.display()

# COMMAND ----------

df2.select(df2.address.city, df2.address.state, df2.age, df2.firstName, df2.gender, df2.lastName, df2.phone.number, df2.phone.type).display()

# COMMAND ----------

df1 = spark.read.option("multiline", "True").json("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/sample2.json")

df1.display()

# COMMAND ----------

def flatten(df):
    # compute Complex Fields (Lists and Structs) in Schema
    complex_fields = dict([(field.name, field.dataType)
                           for field in df.schema.fields
                           if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    while len(complex_fields) != 0:
        col_name = list(complex_fields.keys())[0]
        print("Processing :" + col_name + " Type : " + str(type(complex_fields[col_name])))

        # if StructType then convert all sub element to columns.
        # i.e. flatten structs
        if type(complex_fields[col_name]) == StructType:
            expanded = [col(col_name + '.' + k).alias(col_name + '_' + k) for k in
                        [n.name for n in complex_fields[col_name]]]
            df = df.select("*", *expanded).drop(col_name)

        # if ArrayType then add the Array Elements as Rows using the explode function
        # i.e. explode Arrays
        elif type(complex_fields[col_name]) == ArrayType:
            df = df.withColumn(col_name, explode_outer(col_name))

        # recompute remaining Complex Fields in Schema
        complex_fields = dict([(field.name, field.dataType)
                               for field in df.schema.fields
                               if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    return df


# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import col, explode_outer

df2 = flatten(df1)

df2.display()

# COMMAND ----------

df = spark.read.parquet("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/parquet/userdata1.parquet")

df.display()

df.printSchema()

# COMMAND ----------

df = spark.read.format("avro").load("dbfs:/FileStore/shared_uploads/katsreen100@gmail.com/userdata1.avro")

df.printSchema()

df.display()

# COMMAND ----------

df = spark.read.format('parquet').load("dbfs:/FileStore/parquet/userdata1.parquet")
df.display()
df.printSchema()

print(df.count())

# COMMAND ----------

df = spark.read.format('parquet').load("dbfs:/FileStore/parquet/*.parquet")
df.display()
df.printSchema()

print(df.count())

# COMMAND ----------

df = spark.read.format('csv').load("dbfs:/FileStore/parquet/*.csv", header= True)
display(df)
df.printSchema()

print(df.count())

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TEMPORARY VIEW parquetTable
# MAGIC USING org.apache.spark.sql.parquet
# MAGIC OPTIONS (
# MAGIC   path "dbfs:/FileStore/parquet/userdata1.parquet"
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM parquetTable where id=1

# COMMAND ----------

df = spark.read.format('avro').load("dbfs:/FileStore/avro/userdata1.avro")

df.display()

print(df.count())

df.printSchema()

# COMMAND ----------


data = [("Rahul","Smith","USA","C"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("ramesh","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("rahul","Smith","USA","A"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("Jamessadhfsadhgasfghashgfashdgfghsadfa","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","K"),
    ("Maria","Jones","USA","FL")
  ]

columns = ["firstname","lastname","country","state_name"]
df = spark.createDataFrame(data = data, schema = columns)
df.show(n=2,truncate=False)

# COMMAND ----------

df.count()

# COMMAND ----------

df.rdd.getNumPartitions()

# COMMAND ----------

df.write.csv("dbfs:/FileStore/csvload2/employee2.csv", mode='append', header=True)

# COMMAND ----------

df.write.parquet("dbfs:/FileStore/parload/employee.parquet", mode='append')

# COMMAND ----------

df.write.csv("dbfs:/FileStore/csvload/employee.csv", mode='overwrite')

# COMMAND ----------

spark.read.csv("dbfs:/FileStore/csvload2/employee2.csv", header=True).display()

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from global_temp.global_view

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from employee

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC update employee set country='US' where state_name='A'

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY employee

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT max(version) -1 as permanent_view  FROM (DESCRIBE HISTORY permanent_view)
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC RESTORE TABLE employee  TO VERSION AS OF 0

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from employee

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from employee2 limit 4

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from global_temp.global_employee

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode_outer

# Initialize a Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Create a sample DataFrame with an array column, including null and empty arrays
data = [
    (1, ["a", "b", "c"]),
    (2, ["d", "e"]),
    (3, []),
    (4, None)
]
columns = ["id", "values"]
df = spark.createDataFrame(data, columns)

# Use the explode_outer function to transform the array into multiple rows
df_exploded = df.select(df.id, explode_outer(df.values).alias("value"))
df_exploded.show()


# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode_outer

# Initialize a Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Create a sample DataFrame with a map column, including null maps
data = [
    (1, {"a": 1, "b": 2}),
    (2, {"c": 3, "d": 4}),
    (3, {}),
    (4, None)
]
columns = ["id", "values"]
df = spark.createDataFrame(data, columns)

# Use the explode_outer function to transform the map into multiple rows
df_exploded = df.select(df.id, explode_outer(df.values).alias("key", "value"))
df_exploded.show()


# COMMAND ----------



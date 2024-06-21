from pyspark.sql import SparkSession
from pyspark.sql.types import *  # structType


# Data should be pass as a Tuple and Columns in List to DataFrame
spark = SparkSession.builder.master("local").appName("create data frame").getOrCreate()

print("------------Method1--------------")
dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
column = ['Language', 'fee']
df = spark.createDataFrame(data=dataList, schema=column)
df.show()

print("------------Method2 by StructType = spark.createDataFrame([], StructType([])) --------------")
columns = StructType([
    StructField("ID", IntegerType(), nullable=False),
    StructField("Name", StringType(), nullable=False),
    StructField("Age", FloatType(), nullable=False)
])

data1 =[(1, "Arun", 25.6), (2, "Bharath", 30.4), (3, "Chandan", 35.2)]
df1 = spark.createDataFrame(data = data1, schema=columns)

df1.show()


print("------------Method3 by ZIP dictionary --------------")
# Create DataFrame
names = ["Ricky", "Bunny", "Coco"]
ages = [10, 15, 20]
country = ["India", "UK", "USA"]
data2 = {"Name": names, "Age": ages}

# Creating DataFrame
df2 = spark.createDataFrame(list(zip(*data2.values())), schema=list(data2.keys()))
df2.show()

print("------------Method4 by ZIP List--------------")
df3 = spark.createDataFrame(zip(names, ages, country), ["Name", "Age", "Country"])
df3.show()


print("------------Method5 by List data convert to tuple --------------")
student1 = ["Ricky",10,"India"]
student2 = ["Bunny", 15,"UK"]
student3 = ["Coco", 20, "USA"]

# Define the schema
schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True),
    StructField("Country", StringType(), True)
])

# Convert lists of Data into tuples
data5 = [tuple(student1),
        tuple(student2),
        tuple(student3)]

# Create a DataFrame
df5 = spark.createDataFrame(data5, schema=schema)
df5.show()


spark.stop()
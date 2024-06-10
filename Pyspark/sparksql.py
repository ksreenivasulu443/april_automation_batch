from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.master("local[1]").appName("dataframe").getOrCreate()


data = [("Rahul","Smith","USA","C"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("ramesh","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL")
  ]
columns = ["firstname","lastname","country","state_name"]
df = spark.createDataFrame(data = data, schema = columns)
df.show()

df.createOrReplaceTempView('target')

df2 = spark.sql(""" select upper(firstname) as firstname,lastname from target where lastname='Smith' 
                or state_name ='CA' """)

df2.show()

%sql

select * from target
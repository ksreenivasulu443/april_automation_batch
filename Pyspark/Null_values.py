# Databricks notebook source
df = spark.read.csv("dbfs:/FileStore/parquet/Contact_info.csv", header=True)

# COMMAND ----------

df.display()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.fillna({'middle_initial':'unkwn','suffix':'JR'}).display()

# COMMAND ----------

df2 = spark.read.csv("dbfs:/FileStore/shared_uploads/csv_files/Contact_info-1.csv", header=True, inferSchema=True)

df2.printSchema()

# COMMAND ----------

df2.display()

# COMMAND ----------

df2.fillna({'middle_initial':'unkwn','suffix':'JR'}).fillna(100).display()

# COMMAND ----------

from pyspark.sql.functions import upper, trim

df3 = df2.withColumn('Primary_street_number', when((upper(df2['Primary_street_number']) == "NULL") | (trim(df2['Primary_street_number']) == "" ) | (upper(df2['Primary_street_number']) == "NA" ) , None).otherwise(df2['Primary_street_number']))

df3.display()
df3.fillna({'middle_initial':'unkwn','suffix':'JR','Primary_street_number':'1/22'}).fillna(100).display()




# COMMAND ----------

df5 = df3.withColumn('middle_initial', col('middle_initial').cast('int')).\
withColumn('Identifier', col('Identifier').cast('string'))

df5.printSchema()

df5.display()

# COMMAND ----------

df3.fillna({'middle_initial':'unkwn','suffix':'JR','Primary_street_number':'1/22'}).fillna(100).display()

df3.select(c1,c2,c3, nul(c4,0))

# COMMAND ----------

df2 = spark.read.csv("dbfs:/FileStore/shared_uploads/csv_files/Contact_info-1.csv", header=True, inferSchema=True)

df2.display()

# COMMAND ----------

df.dropna(subset=['identifier']).display()

# COMMAND ----------

collect_out = df.collect()

type(collect_out)

# COMMAND ----------


type(df.first())

# COMMAND ----------

print(collect_out)

print(len(collect_out))

collect_out[0]

# COMMAND ----------

collect_out[0]['Primary_street_number']

# COMMAND ----------

df4.select("Primary_street_number").filter('identifier=1').collect()[0][0]

# COMMAND ----------

df4.display()

# COMMAND ----------

df3.sample(0.2, seed=4).display()

# COMMAND ----------

df3.sample(fraction=0.3, seed=8, withReplacement=True).display()

# COMMAND ----------

df= df.drop('Surname')

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.drop('given_name', 'suffix','identifier')

# COMMAND ----------

df.display()

# COMMAND ----------

df4 = spark.read.csv("dbfs:/FileStore/shared_uploads/csv_files/Contact_info-1.csv", header=True, inferSchema=True)

df4.display()

# COMMAND ----------

df4.createOrReplaceTempView('df4')

# COMMAND ----------

df.distinct().display()

# COMMAND ----------

df.dropDuplicates(['city']).display()

df.dropDuplicates().display()

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when,upper, trim,expr


data = [
    (1, "Alice", None),
    (2, "Bob", 45),
    (3, 'NULL', 29),
    (4, "Catherine", ''),
    (5, "null", '  '),
    (6, "na", 'NULL'),
    (7, None, 'NULL')
]
columns = ["ID", "Name", "Age"]
df = spark.createDataFrame(data, columns)
df.fillna(0).fillna('unkwn').display()
# Display the original DataFrame
#df.show()

# Drop rows with any null values
# df_dropna = df.dropna()
# df_dropna.show()

# # Drop rows with null values in specific columns
# df_dropna_subset = df.dropna(subset=["Name"])
# df_dropna_subset.show()




# COMMAND ----------

# Fill null values with specific values
df.display()
# Replace null values in a specific column
df2 = df.withColumn("name", expr("""case when upper(name)='NULL' then null when trim(name)='' then null when upper(name)='NA' then null else name end  """)).withColumn("age",expr("case when upper(age)='NULL' then null else age end"))
df2.display()

df_fillna = df2.fillna({"Name": "Unknown", "Age": 0})
df_fillna.show()


# COMMAND ----------



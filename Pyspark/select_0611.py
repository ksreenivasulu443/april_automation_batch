# Databricks notebook source
from pyspark.sql import SparkSession

from pyspark.sql.functions import col,upper, lower, length, concat, initcap, explode, substring, instr,concat_ws, expr,lit

data = [("Rahul","Smith","USA","C"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("Robert","Williams","USA","K"),
    ("Maria","Jones","USA","FL")
  ]
columns = ["first name","lastname","country","state_name"]
df = spark.createDataFrame(data = data, schema = columns)
df.show()

id(df)



# COMMAND ----------

df3 = df.select(df.firstname, df.lastname)

df3.show()

type(df3)


# COMMAND ----------

df.select(col('firstname'), col('lastname')).show(2)


# COMMAND ----------

df.select(df['firstname'], df['lastname'], df['country'], df['state_name']).show(2)


# COMMAND ----------

df5 = df.select(upper('firstname').alias('fn'), lower('lastname').alias('ln'), 'state_name',length('state_name').alias("state_name_length"))
df5.show()

df5.createOrReplaceTempView("df5")

spark.sql("select * from df5")

# COMMAND ----------

df.createOrReplaceTempView('source')

# COMMAND ----------

spark.sql("select upper(firstname) fn, lower(lastname) ln , state_name, length(state_name) state_name_length from source").show()


df = spark.sql("select upper(firstname) fn, lower(lastname) ln , state_name, length(state_name) state_name_length, 'US' as country_code from source")
df.show()
# id(df)

139776549024240
139776549024240

# COMMAND ----------

df.show()

# COMMAND ----------

df.select(df.colRegex("`^.*name*`")).show()


# COMMAND ----------

df.select('*', lit('USA').alias("country_code")).show(2)


# COMMAND ----------

# df.select('firstname','lastname').where(" firstname = 'Rahul'  ").show()

# df.select('firstname','lastname').filter(" firstname = 'Rahul' ").show()

df.show()


# COMMAND ----------

df.where("('first name' = 'Rahul' or lastname ='Rose') and state_name='NY'  ").show()

df.select("*").filter( ((df['first name'] == 'Rahul') | (df.lastname== 'Rose' )) & ( df.state_name=='NY')).show()

# COMMAND ----------



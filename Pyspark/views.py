# Databricks notebook source
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

# COMMAND ----------

df.createOrReplaceTempView('target')

df.createTempView("target2")

# COMMAND ----------

df.createOrReplaceTempView('target2')

df.createTempView("target2")

# COMMAND ----------


df3 = spark.read.csv("dbfs:/FileStore/Contact_info.csv", header=True)

df3.display()

# COMMAND ----------

df2 = spark.sql(""" select upper(firstname),lastname from target where lastname='Smith' 
                or state_name ='CA' """)

# COMMAND ----------

df2.show()

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select upper(firstname),lastname from target where lastname='Smith' 
# MAGIC                 or state_name ='CA' 

# COMMAND ----------

df.createGlobalTempView("global_source2")

# COMMAND ----------

df.createOrReplaceGlobalTempView("global_source2")

# COMMAND ----------

df2 = spark.sql(""" select upper(firstname),lastname from global_temp.global_source2 where lastname='Smith' 
                or state_name ='CA' """)
df2.show()

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from global_temp.global_source

# COMMAND ----------

df.write.saveAsTable("permanent_view")

# COMMAND ----------

spark.sql("select * from target").show()

# COMMAND ----------



# Databricks notebook source
from pyspark.sql.functions import lit

df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])

df.show()


# COMMAND ----------

df.createOrReplaceTempView('df')

# COMMAND ----------

df2 = spark.sql("select df.*, 30 as Age from df")

df2.show()

# COMMAND ----------

df3 = df.select(id, upper(name) as name, lit(30).alias('Age'))

df3.show()

# COMMAND ----------

# Add a new column 'age' with a constant value
df4 = df.withColumn("Age", lit(20)).withColumn("country",lit("USA")).withColumn("state",lit("NY"))

df4.show()

df4.printSchema()

# COMMAND ----------

df.show()

# COMMAND ----------

from pyspark.sql.functions import col, upper, expr

# Update the 'name' column to uppercase
df5 = df.withColumn("name", upper(col("name")))

df5.show()


# COMMAND ----------

df.show()

# COMMAND ----------

df6 = df.withColumn("roll_num_word", expr("""case when id=1 then 'one' else 'two' end roll_num_word""" ))

df6.show()

# COMMAND ----------

spark.sql("select id, name as firstname, case when id=1 then 'one' else 'two' end roll_num_word from df").show()

# COMMAND ----------

df.select('id',col('name').alias('firstanme'), expr("""case when id=1 then 'one' else 'two' end roll_num_word""")).show()

# COMMAND ----------

df4 = df.withColumn("dense_rank", expr('''dense_rank() over(order by id desc)''' ))

df4.show()

# COMMAND ----------

df.show()

# COMMAND ----------

df7 = df.withColumnRenamed("name","first_name").withColumnRenamed('id','Identifier')

df7.show()

# COMMAND ----------

df4.show()

# COMMAND ----------



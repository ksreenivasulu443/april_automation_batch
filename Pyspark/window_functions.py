# Databricks notebook source
simpleData = (("James", "Sales", 3000), \
              ("Michael", "Sales", 4600), \
              ("Robert", "Sales", 4100), \
              ("Maria", "Finance", 3000), \
              ("James", "Sales", 3000), \
              ("Scott", "Finance", 3300), \
              ("Jen", "Finance", 3900), \
              ("Jeff", "Marketing", 3000), \
              ("Kumar", "Marketing", 2000), \
              ("Saif", "Sales", 4100) \
              )

columns = ["employee_name", "department", "salary"]
df = spark.createDataFrame(data=simpleData, schema=columns)
df.printSchema()
df.show(truncate=False)

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import *

# COMMAND ----------

window1 = Window.partitionBy('department').orderBy(df['salary'].desc())

# COMMAND ----------

df.createOrReplaceTempView('tb')

# COMMAND ----------


spark.sql("""select tb.* , rank() over( partition by department order by salary desc) rank from tb """).show()

# select a.* , rank() over( order by salary desc) dense_rank from tb a

# select a.* , row_number() over( order by salary desc) dense_rank from tb a


# COMMAND ----------

# df.withColumn('rank', rank().over(Window.partitionBy('department').orderBy(df['salary'].desc()))).display()


# df.withColumn('drank', dense_rank().over(Window.partitionBy('department').orderBy(df['salary'].desc()))).display()

# df.withColumn('row_num', row_number().over(Window.partitionBy('department').orderBy(df['salary'].desc()))).display()

df.withColumn('row_num', expr("row_number() over( order by salary desc) dense_rank")).withColumn("newcol", logic).display()

# emp.sort(emp.eno.desc(), emp.salary.asc()).show()
# emp.orderBy(emp.eno.asc()).show()

# COMMAND ----------



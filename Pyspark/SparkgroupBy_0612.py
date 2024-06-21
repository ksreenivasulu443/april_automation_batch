# Databricks notebook source

from pyspark.sql.functions import sum, avg, min, max, count, round,ceil, floor

simpleData = [("James", "Sales", "NY", 90000, 34, 10000),
              ("James", "Sales", "NY", 86000, 56, 20000),
              ("Robert", "Sales", "CA", 81000, 30, 23000),
              ("Maria", "Finance", "CA", 90000, 24, 23000),
              ("Raman", "Finance", "CA", 99000, 40, 24000),
              ("Scott", "Finance", "NY", 83000, 36, 19000),
              ("Jen", "Finance", "NY", 79000, 53, 15000),
              ("Jeff", "Marketing", "CA", 80000, 25, 18000),
              ("", "Marketing", "NY", 91000, 50, 21000)
              ]

schema = ["employee_name", "department", "state", "salary", "age", "bonus"]
df = spark.createDataFrame(data=simpleData, schema=schema)
df.printSchema()
df.show(truncate=False)

# COMMAND ----------

summary2 = df.summary()
summary2.display()

# COMMAND ----------

summary3 = df.select('salary', 'age','bonus').summary()
summary3.show()

# COMMAND ----------


summary2 = df.summary()
summary2.display()
summary2.select('summary', 'state', 'salary', 'bonus').where("summary in ('count','max','min') ").display()

# COMMAND ----------

df.createOrReplaceTempView("source")
spark.sql( """
select 'salary' column ,sum(salary) as sum_salry, min(salary) min_salary, max(salary) max_salary, count(1) cnt, round(avg(salary),2) avg_salary from source  """).display()


# COMMAND ----------

from pyspark.sql.functions import lit

# COMMAND ----------

df10= df.select(lit("salry").alias("column"),sum('salary').alias("sum_sal"), \
          count("*").alias("num_of_records"), \
          avg('salary').alias("average_sal"), \
          min('salary').alias("min_sal"), \
          max('salary').alias("max_sal"))


df10.display()


# COMMAND ----------


spark.sql("""select department, sum(salary), avg(salary), min(salary) from source group by department""").show()

# COMMAND ----------

df.groupBy('department','state').sum('salary').count().max()
# df.groupBy('department').min().show()
# df.groupBy('department').max().show()

# df.groupBy('department').avg().show()

df.groupBy('department').count().show()



# COMMAND ----------

spark.sql("""
select department, state, sum(salary) from source group by all""").display()

# COMMAND ----------

df.groupBy("department", "state").sum('bonus').show()

# COMMAND ----------

spark.sql("select employee_name , count(1) from source group by all having count(1)>1").show()

# COMMAND ----------

df.groupBy("employee_name").count().where('count>1').show()

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select department, sum(salary), round(avg(salary)), min(salary), sum(bonus), min(salary), count(1) from source group by department

# COMMAND ----------

from pyspark.sql.functions import ceil, floor

df.groupBy("department") \
    .agg(sum("salary").alias("sum_salary"),
         avg("salary").alias("avg_salary"), \
         round(avg("salary")).alias("avg_salary"), \
         sum("bonus").alias("sum_bonus"), \
         max("bonus").alias("max_bonus"), \
         min("salary").alias("min_sal"), \
         count('department').alias('num_emp')
         ) \
    .show(truncate=False)

# df.groupBy('department','state').sum('salary').show()
# # df.groupBy('department').min().show()
# # df.groupBy('department').max().show()

# # df.groupBy('department').avg().show()

# df.groupBy('department').count().show()

# COMMAND ----------



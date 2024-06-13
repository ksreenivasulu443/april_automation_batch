# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC #Joins

# COMMAND ----------

# MAGIC %md
# MAGIC ## Dataframe definition
# MAGIC

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ### emp df

# COMMAND ----------

# DBTITLE 1,This is code to create simple spark dataframe using list of tuple values
emp = [(1, "Smith", -1, "2018", "10", "M", 3000), \
       (2, "Rose", 1, "2010", "20", "M", 4000), \
       (3, "Williams", 1, "2010", "30", "M", 1000), \
       (4, "Jones", 10, "2005", "10", "F", 2000), \
       (5, "Brown", 2, "2010", "40", "", 1000), \
       (6, "Brown", 2, "2010", "50", "", 500) \
       ]
empColumns = ["eno", "ename", "mgr_id", "year_joined", \
              "dept_id", "gender", "salary"]

emp = spark.createDataFrame(data=emp, schema=empColumns)
emp.printSchema()
emp.show(truncate=False)

dept = [("Finance", 10,'NY'), \
        ("Marketing", 20,"CA"), \
        ("Sales", 30,'NJ'), \
        ("IT", 40,'CA'),
        ("HR", 60,'NJ') \
        ]
deptColumns = ["dept_name", "dept_id","loc"]
dept = spark.createDataFrame(data=dept, schema=deptColumns)
dept.printSchema()
dept.show(truncate=False)



# COMMAND ----------

# MAGIC %md
# MAGIC ## inner join

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select eno, ename, mgr_id, year_joined, dept_id, gender, salary, dept_name from emp inner join dept on emp.dept_id = dept.dept_id

# COMMAND ----------

# join_df = emp.join(dept, emp.dept_id == dept.dept_id , how='inner').\
#         drop(dept.loc, dept.dept_id, emp.mgr_id)

# join_df.display()
emp1 = emp.select('ename','salary','dept_id')
dept1 = dept.select('dept_id', 'loc')
emp1.join(dept1, 'dept_id', 'inner').display()


emp.select('ename','salary','dept_id').join(dept.select('dept_id', 'loc'),'dept_id', 'inner').display()

# COMMAND ----------

emp.join(dept, ['dept_id'], 'inner').show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Left join

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'left').show()

emp.join(dept, 'dept_id', 'left').show()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## right join

# COMMAND ----------

# emp.join(dept, emp.dept_id == dept.dept_id, 'right').show()
from pyspark.sql.functions import col
emp.alias('emp').join(emp.alias('emp2'), col('emp.eno') == col('emp2.mgr_id'), how= 'inner').display()




# empDF.alias("emp1").join(empDF.alias("emp2"), \
#     col("emp1.superior_emp_id") == col("emp2.emp_id"),"inner") \
#     .select(col("emp1.emp_id"),col("emp1.name"), \
#       col("emp2.emp_id").alias("superior_emp_id"), \
#       col("emp2.name").alias("superior_emp_name")) \
#    .show(truncate=False)

# COMMAND ----------

emp.join(other = dept, on = emp.dept_id == dept.dept_id, how='fullouter').show()


# COMMAND ----------

emp.createOrReplaceTempView('emp')
dept.createOrReplaceTempView('dept')

# COMMAND ----------

spark.sql("select * from emp where dept_id in ( select dept_id from dept)").display()

# COMMAND ----------



emp.join(dept, emp.dept_id == dept.dept_id, 'inner').show() 

emp.join(dept, emp.dept_id == dept.dept_id, 'leftsemi').show() 



# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC

# COMMAND ----------

emp.show()
dept.show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, 'left_anti').show()

spark.sql("""select emp.* from emp  left join dept  on emp.dept_id=dept.dept_id where dept.dept_id is null""").show()

# emp.join(dept, emp.dept_id == dept.dept_id, 'left').show() 

# COMMAND ----------

from pyspark.sql.functions import broadcast

emp.join(broadcast(dept), emp.dept_id == dept.dept_id, how='left').show()

# COMMAND ----------

emp.join(dept, emp.dept_id == dept.dept_id, how='left').show()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Set oprators

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## union

# COMMAND ----------



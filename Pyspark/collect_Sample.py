# Databricks notebook source
df = spark.read.csv("dbfs:/FileStore/shared_uploads/csv_files/Contact_info-1.csv", header=True, inferSchema=True)

df.display()

# COMMAND ----------

df.sample(0.5).display()

#df.sample?

# COMMAND ----------

df.sample(fraction=0.3, seed=5, withReplacement=False).display()

# COMMAND ----------

df = df.drop(*df.columns)

df.show()

del df


# COMMAND ----------

df.distinct().display()
df.select('*').distinct().display()

# select distinct identifier from tn

# COMMAND ----------

df = df.dropDuplicates(['Identifier']).display()

df.dropDuplicates().display()

# COMMAND ----------

df2 = spark.read.csv("dbfs:/FileStore/shared_uploads/csv_files/Contact_info-1.csv", header=True, inferSchema=True)
df2.display()
#df2.display()

actual_name = df2.select('given_name').filter("given_name='Sreenivasulu' ").collect()[0][0]
print(actual_name)
print(type(actual_name))

expected_name = 'Sreenivasulu'

print(type(expected_name))

if expected_name == actual_name:
    print("True")



# collect_out = df.collect()

# type(collect_out)
# type(df.first())
# collect_out[0]
#df2.select("Primary_street_number").filter('identifier=1').collect()[0][0]

# COMMAND ----------

print(df2.collect()[0][1:10])

print(df2.collect())

# COMMAND ----------

type(df2.count())

df2.count()

# COMMAND ----------

print(type(df2.first()))

df2.collect()[0]
df2.first()

# COMMAND ----------

from pyspark.sql.functions import udf,lower, upper, instr, substring,length, regexp_extract
from pyspark.sql.types import StringType



# Define the age categorization function
def categorize_age(age):
    if age < 20:
        return "Teen"
    elif 20 <= age < 40:
        return "Adult"
    elif age >= 40:
        return "Senior"
    else:
        return None
    

categorize_age(20)
# Register the function as a UDF
categorize_age_udf = udf(categorize_age, StringType())

# Create the source DataFrame
source_data = [(1, 15), (2, 25), (3, 35), (4, 45), (5, 55)]
source_df = spark.createDataFrame(source_data, ["user_id", "age"])

# Apply the UDF to transform the age column
transformed_df = source_df.withColumn("age_category", categorize_age_udf(source_df["age"]))

# Create the target DataFrame
transformed_df.show()





# COMMAND ----------

def categorize_age(age):
    if age < 20:
        return "Teen"
    elif 20 <= age < 40:
        return "Adult"
    elif age >= 40:
        return "Senior"
    else:
        return None
    

categorize_age(19)

# COMMAND ----------

from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("PivotExample").getOrCreate()

# Create DataFrame
data = [("2023-01-01", "A", 100), ("2023-01-01", "B", 150), 
        ("2023-01-02", "A", 200), ("2023-01-02", "B", 250)]
df = spark.createDataFrame(data, ["Date", "Product", "Sales"])
df.show()
# Pivot the DataFrame
df.groupBy("Date").pivot("Product").sum("Sales").show()

pivot_df = df.groupBy("Date").sum("Sales")
pivot_df.show()


# COMMAND ----------

from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("UnpivotExample").getOrCreate()

# Create DataFrame
data = [("2023-01-01", 100, 150), ("2023-01-02", 200, 250)]
df = spark.createDataFrame(data, ["Date", "A", "B"])

# Unpivot the DataFrame
unpivot_expr = "stack(2, 'A', A, 'B', B) as (Product, Sales)"
unpivot_df = df.selectExpr("Date", unpivot_expr)
unpivot_df.show()


# COMMAND ----------

from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("PivotExample2").getOrCreate()

# Create DataFrame
data = [("2023-01-01", "John", "HR", 8), ("2023-01-01", "Alice", "IT", 6), 
        ("2023-01-01", "Bob", "HR", 7), ("2023-01-02", "Alice", "IT", 8), 
        ("2023-01-02", "Bob", "HR", 6)]
df = spark.createDataFrame(data, ["Date", "Employee", "Department", "Hours"])
df.show()
# # Pivot the DataFrame to show total hours per department for each date
# pivot_df = df.groupBy("Date").pivot("Department").sum("Hours")
# pivot_df.show()


# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

spark.udf.register("categorize_age", categorize_age, StringType())
source_df.createOrReplaceTempView('df')
spark.sql("""
    SELECT user_id, age, categorize_age(age) AS age_category
    FROM df
""").show()

df.select

# transformed_df = source_df.withColumn("age_category", categorize_age(source_df["age"]))

# COMMAND ----------

from pyspark.sql.functions import cate

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

def squared(x):
    return x * x


# COMMAND ----------

from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType


# Register the UDF
squared_udf = udf(squared, IntegerType())

data = [(1,), (2,), (3,), (4,)]
df = spark.createDataFrame(data, ["number"])

# Apply the UDF
df_with_squared = df.withColumn("squared", squared_udf(df["number"]))
df_with_squared.show()


# COMMAND ----------

from pyspark.sql.functions import udf
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



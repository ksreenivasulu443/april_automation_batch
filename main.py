import datetime
import sys

import pandas as pd
import openpyxl
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_set
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from utility.read_utility import read_file, read_db, read_snowflake
from utility.validation_lib import count_check, duplicate_check, uniqueness_check, records_present_only_in_source, \
    null_value_check, data_compare, name_check, column_range_check, column_value_reference_check, schema_check

project_path = os.getcwd()

postgre_jar = project_path + "/jars/postgresql-42.2.5.jar"
snow_jar = project_path + "/jars/snowflake-jdbc-3.14.3.jar"
#oracle_jar = project_path + "/jars/ojdbc11.jar"

jar_path = postgre_jar+','+snow_jar
spark = SparkSession.builder.master("local[5]") \
    .appName("test") \
    .config("spark.jars", jar_path) \
    .config("spark.driver.extraClassPath", jar_path) \
    .config("spark.executor.extraClassPath", jar_path) \
    .getOrCreate()
#


print("*"*50)
print(postgre_jar)
print(jar_path)
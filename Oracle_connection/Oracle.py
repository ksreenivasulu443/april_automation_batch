import datetime
import json
import os
import sys
from pyspark.sql.functions import explode_outer, concat, col, \
    trim,to_date, lpad, lit, count,max, min, explode, current_timestamp
# import getpass
#
# from pyspark.sql import SparkSession
# spark = SparkSession.builder.master("local[2]") \
#     .appName("test") \
#     .config("spark.jars", r'C:\Users\om\PycharmProjects\april_automation_batch\jars\ojdbc8-23.2.0.0.jar') \
#     .config("spark.driver.extraClassPath", r'C:\Users\om\PycharmProjects\april_automation_batch\jars\ojdbc8-23.2.0.0.jar') \
#     .config("spark.executor.extraClassPath", r'C:\Users\om\PycharmProjects\april_automation_batch\jars\ojdbc8-23.2.0.0.jar') \
#     .getOrCreate()
#
# df2 = spark.read.format("jdbc"). \
#     option("url", "jdbc:oracle:thin:@//localhost:1521/xe"). \
#     option("user", "System"). \
#     option("password", "Admin"). \
#     option("query", "select * from tab"). \
#     option("driver", "oracle.jdbc.driver.OracleDriver").load()
#
# df2.show(30)
#
# system_user = getpass.getuser()
#
# batch_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# df2 = df2.withColumn('batch_date', lit(batch_id))\
#     .withColumn('create_date', current_timestamp())\
#     .withColumn('update_date', current_timestamp())\
#     .withColumn('create_user',lit(system_user))\
#     .withColumn('update_user',lit(system_user))

# df2.write.mode("overwrite") \
#     .format("jdbc") \
#     .option("url", "jdbc:oracle:thin:@//localhost:1521/freepdb1") \
#     .option("dbtable", "contact_info_updated") \
#     .option("user", "scott") \
#     .option("password", "tiger") \
#     .option("driver", 'oracle.jdbc.driver.OracleDriver') \
#     .save()
#

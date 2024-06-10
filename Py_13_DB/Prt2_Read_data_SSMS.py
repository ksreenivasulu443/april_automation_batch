# from pyspark.shell import sqlContext
from pyspark.python.pyspark.shell import sqlContext
from pyspark.sql import SparkSession

# Initialize SparkSession
# spark = SparkSession.builder \
#     .appName("PySpark SQL Server Query") \
#     .config("spark.jars", r"C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\mssql-jdbc-11.2.0.jre8.jar") \
#     .getOrCreate()

spark = SparkSession.builder.master("local") \
    .appName("test") \
    .config("spark.jars", r'C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\mssql-jdbc-11.2.0.jre8.jar') \
    .config("spark.driver.extraClassPath", r'C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\mssql-jdbc-11.2.0.jre8.jar') \
    .config("spark.executor.extraClassPath", r'C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\mssql-jdbc-11.2.0.jre8.jar') \
    .getOrCreate()

# JDBC URL and connection properties jdbc:sqlserver://;serverName=demoserver443.database.windows.net.database.windows.net;databaseName=sampledb
# jdbc_url = "jdbc:sqlserver://;serverName='DESKTOP-MUUV9KR\MSSQLSERVER2022';databaseName='70-461'"
# connection_properties = {
#     "user": "sa",
#     "password": "Sqlserver@ssms",
#     "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
# }

# Load data from the database into a DataFrame
df = sqlContext.load(
  source="jdbc",driver="SQL SERVER",
  url="jdbc:h2:tcp://DESKTOP-MUUV9KR/~/test?user=sa&password=Sqlserver@ssms",
  dbtable="EMP"
)
# df = spark.read.jdbc(url=jdbc_url, table="EMP", properties=connection_properties)
# df = spark.read \
#     .format("jdbc") \
#     .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
#     .option("url", jdbc_url) \
#     .option("dbtable", 'EMP')     \
#     .load()

# Show the first few rows of the DataFrame
df.show()

# Perform transformations
# filtered_df = df.filter(df["some_column"] > 10).select("column1", "column2")
#
# # Show the result of the transformations
# filtered_df.show()

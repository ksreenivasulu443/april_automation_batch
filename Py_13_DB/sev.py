from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.master("local") \
    .appName("test") \
    .config("spark.jars", r'C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\snowflake-jdbc-3.14.3.jar') \
    .config("spark.driver.extraClassPath", r'C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\snowflake-jdbc-3.14.3.jar') \
    .config("spark.executor.extraClassPath", r'C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\snowflake-jdbc-3.14.3.jar') \
    .getOrCreate()


jdbc_url = "jdbc:sqlserver://;serverName='DESKTOP-MUUV9KR\MSSQLSERVER2022';databaseName='70-461'"

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:sqlserver://;serverName=DESKTOP-MUUV9KR\MSSQLSERVER2022;databaseName=master") \
    .option("dbtable", "emp") \
    .option("user", "sa") \
    .option("password", "Sqlserver@ssms") \
    .load()

df.show()





# query = "(select * from emp) as emp"
# username = 'sa'
# password = 'Sqlserver@ssms'
# jdbc_url = "jdbc:sqlserver://DESKTOP-MUUV9KR:15776;database=master"
#
#
# df = spark.read \
#         .format("com.microsoft.sqlserver.jdbc.spark") \
#         .option("url", jdbc_url) \
#         .option("dbtable", query) \
#         .option("user", username) \
#         .option("password", password).load()
#
# df.show()

# # Initialize the Spark session
# spark = SparkSession.builder \
#     .appName("SQL Server Data Retrieval") \
#     .config("spark.jars", r"C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\mssql-jdbc-11.2.0.jre8.jar") \
#     .getOrCreate()
#
# # Define the connection properties
# jdbc_url = "jdbc:sqlserver://DESKTOP-MUUV9KR:15776;databaseName=master"
# connection_properties = {
#     "user": "sa",
#     "password": "Sqlserver@ssms",
#     "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
# }
#
# # Define your query
# query = "(SELECT * FROM EMP) AS EMP"
#
# # Load the data into a DataFrame
# df = spark.read.jdbc(url=jdbc_url, table=query, properties=connection_properties)
#
# df.show()

# Stop the Spark session
spark.stop()

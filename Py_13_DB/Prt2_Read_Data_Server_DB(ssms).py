from pyspark.sql import SparkSession

#Connection details
CONNECTOR_TYPE = "com.microsoft.sqlserver.jdbc.spark"
SQL_USERNAME = "sa"
SQL_PASSWORD = "Sqlserver@ssms"
SQL_DBNAME = "Sample_70_461"
SQL_SERVER_NAME = "DESKTOP-MUUV9KR\MSSQLSERVER2022"
#Table name
Table_Name = "dbo.EMP"
Jar_path = r'C:\Users\User\PycharmProjects\pyspark\april_automation_batch\jar\mssql-jdbc-11.2.0.jre8.jar'

# Initialize SparkSession
spark = SparkSession.builder.master("local") \
    .appName("test") \
    .config("spark.jars", Jar_path) \
    .config("spark.driver.extraClassPath", Jar_path) \
    .config("spark.executor.extraClassPath", Jar_path) \
    .getOrCreate()


url = f"jdbc:sqlserver://{SQL_SERVER_NAME}:15776;databaseName={SQL_DBNAME};encrypt=false;trustServerCertificate=true"

df_emp = (spark.read.format(CONNECTOR_TYPE)
          .option("url", url)
          .option("dbtable", Table_Name)
          .option("user", SQL_USERNAME)
          .option("password", SQL_PASSWORD)
          .load())

# df_emp.show()

df_emp.select("EMPNO", "ENAME", "JOB").where("DEPTNO='20'").show()
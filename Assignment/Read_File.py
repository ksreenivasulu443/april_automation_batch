import findspark

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master('local') \
    .appName('myAppName') \
    .config('spark.executor.memory', '5gb') \
    .config('spark.cores.max', '6') \
    .getOrCreate()


# def read_scr(path):
#     print("i am reading data from :", path)
#     a = spark.read.csv(path)
#     src = a.createOrReplaceTempView("src_emp")
#     scr_qry = spark.sql(f"select count(*) from {src}")
#     return scr_qry
#
#
# def read_trg(path):
#     print("i am reading data from :", path)
#     a = spark.read.csv(path)
#     trg = a.createOrReplaceTempView("src_emp")
#     scr_qry = spark.sql(f"select count(*) from {trg}")
#     return scr_qry




# target = read_trg('D:/ETL_Automation/emp2.csv')


# def scr_cnt(sou):
#     scr_qry = spark.sql(f"select count(*) as sorce_count from {sou}")
#     return scr_qry
#
# scr_cnt(read_scr())

# print(read_scr(source = 'D:/ETL_Automation/emp1.csv'))

scr_pth = r"D:/ETL_Automation/emp1.csv"
df = spark.read.csv(scr_pth)

df.createOrReplaceTempView("scr_emp")

scr_cnt = spark.sql("select count(*) from scr_emp")
print(scr_cnt.show())
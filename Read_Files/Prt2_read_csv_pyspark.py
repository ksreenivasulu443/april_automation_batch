import findspark
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master('local') \
    .appName('myAppName') \
    .config('spark.executor.memory', '5gb') \
    .config("spark.cores.max", "6") \
    .getOrCreate()


def read_fun(path):
    print("i am reading data from :", path)
    a = spark.read.format('csv').options(header='true', inferSchema='true').load(path)
    return a


source = read_fun('D:/ETL_Automation/emp1.csv')
target = read_fun('D:/ETL_Automation/emp2.csv')


def count_check(source, target):
    ls=[]
    lt=[]
    source.createOrReplaceTempView("emp1")
    target.createOrReplaceTempView("emp2")
    scr_cnt = spark.sql("SELECT count(*) as scr_cnt FROM emp1")
    trg_cnt = spark.sql("SELECT count(*) as scr_cnt FROM emp2")
    scr_cnt1 = scr_cnt.show()

    trg_cnt1 = trg_cnt.show()

    if scr_cnt1 == trg_cnt1:
        print(f"count is matching: source count is {scr_cnt1} and target count is {trg_cnt1}")
    return scr_cnt1, trg_cnt1

print(count_check(source, target))


# path = "D:/ETL_Automation/emp1.csv"
# df = spark.read.format('csv').options(header='true', inferSchema='true').load(path)
# # df = spark.read.csv(path)
# df.createOrReplaceTempView("emp1")
#
# scr = spark.sql("SELECT count(*) as scr_cnt FROM emp1")
# scr1 = spark.sql("SELECT * FROM emp1")
# print(scr1.show())
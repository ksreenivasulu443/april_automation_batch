import pandas as pd
from pandasql import sqldf


source = pd.read_csv('D:/ETL_Automation/emp1.csv')
target = pd.read_csv('D:/ETL_Automation/emp2.csv')

df_parquet = pd.read_parquet(r"D:\ETL_Automation\ReadFiles\userdata1.parquet", engine='pyarrow')
# print(df_parquet)

df_csv = pd.read_csv(r"D:\ETL_Automation\ReadFiles\Contact_info.csv")
# print(df_csv)

df_excel = pd.read_excel(r"D:\ETL_Automation\ReadFiles\Master_Test_Template.xlsx")
# print(df_excel)

print(sqldf("""select * from df_parquet 
where id in('996', '997')
"""))

print(sqldf("""select count(*) from df_csv """))

print(sqldf("""select count(*) from df_csv """))

print(sqldf("""select EMPNO, ENAME, JOB, MGR, SAL, COMM, DEPTNO, Hiredate from source 
except  
select EMPNO, ENAME, JOB, MGR, SAL, COMM, DEPTNO, Hiredate from target"""))


# select Top Nth records
print("select Top Nth records")
print(df_parquet.head(4))

# select Bottom Nth records
print("select Bottom Nth records")
print(df_parquet.tail(4))

# select describe tabel
print("describe tabel")
print(df_parquet.describe())

# display single column
print("selecting single column")
print(source["ENAME"])
print(type(source["ENAME"]))

# display two column
print("selecting two column")
print(source[["EMPNO","ENAME"]])
print(type(source[["EMPNO","ENAME"]]))

# display all column names
print("all column names")
print(source.columns)

# display all column names with data type
print("all column names with data type")
print(source.dtypes)

# iloc function selecting rows by index
print("iloc function selecting 1st rows by index")
print(source.iloc[0])

print("iloc function selecting 2 rows by index")
print(source.iloc[0:2])

print("iloc function selecting 2 rows by index and 2 column by index")
print(source.iloc[0:2, 0:5])

# loc function selecting rows by index
print("loc function selecting 1st rows by index")
print(source.loc[0:3, "JOB":"DEPTNO"])
print(source.loc[:, "JOB":"DEPTNO"])
print(source.loc[0:3, :])

# Filter function selecting values

print("selective values")
print(source[source['SAL'] <1000])

print(source[(source['SAL'] <1000) & (source['DEPTNO']==20)])
print(source[(source.SAL <1000) & (source.DEPTNO==30)])



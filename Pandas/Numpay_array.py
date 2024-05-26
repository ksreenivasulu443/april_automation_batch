# import numpy as np
#Bool<int<float<str
import pandas as pd
#
# arr=np.array([1,2,3,'sreeni'])
# print("type of arr",type(arr))
# print("value os arr[0] and type of arr[0]",arr[0],type(arr[0]))
#
# ls=[1,2,3,'10.2']
# print("type of ls",type(ls))
# print("value os ls[0] and type of ls[0]",ls[0],type(ls[0]))
#
# series = pd.Series([1,2,3,4],index=['a','b','c','d'])
# print("type of series",type(series))

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago'],
        'Sal':[100,200,300]}
df = pd.DataFrame(data)
print(df)

df2=pd.DataFrame([11,12,13,14],columns=['sno'],index=['a','b','c','d'])
print(df2)

print(help(pd.read_csv))


import pyarrow
from pandasql import sqldf

print("reading csv files")
source = pd.read_csv(r"C:\Users\mahab\PycharmProjects\april_automation_batch\Files\Contact_info.csv")
target =pd.read_csv(r"C:\Users\mahab\PycharmProjects\april_automation_batch\Files\Contact_info_t.csv")
print("print read_csv",source)

# print("reading parquet files")
# source_par = pd.read_parquet(r"C:\Users\mahab\PycharmProjects\april_automation_batch\Files\userdata1.parquet")
# print("print parquet_files",source_par)
#
# print("reading json files")
# source_json = pd.read_json(r"C:\Users\mahab\PycharmProjects\april_automation_batch\Files\sample1.json")
# print("print parquet_files",source_json)

# print(sqldf(''' select * from source where identifier=1
#               or Surname='Kattubadi' '''))
# print(sqldf((''' select * from source except select * from target
#              ''')))

print(source.head(2))
# print(source.tail(2))
print(source.describe())

print("select identifier column data")
print(source[['Identifier','Phone','birthmonth']])

print("select all columns with data types")
print(source.columns)
print(source.dtypes)

print(source[(source['Identifier']>9)])

print(source[(source['Identifier']>5) & (source['Surname'] == 'Arun')])

#add new column
df['Salary']=[7000,8000,9000]


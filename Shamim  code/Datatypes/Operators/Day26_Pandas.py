#Numpy array:

import numpy as np

arr = np.array([1,2,3,'10.4'])#its converts int,float,bool to string
print("type of arr",type(arr))

ls = [1,2,3]
print("type of ls",type(ls))

import  pandas as pd #panda is library
series = pd.Series([1,2,3,4])
print("type of series",type(series))
print(series)#Series is one column in data frame

#source_par = pd.read_parquet (""
# print(source_par)read_excel("")
#source_excel pd.read_excel("

from pandasql import sqldf # pandassql is the package

import pandas as pd
data = {'name': ['shamim','rehan'],'Age':[20,30],'city':['pune','hyd']}

print("type of data",type(data))
df = pd.DataFrame(data)
print(df)

df = pd.read_csv(filepath_or_buffer=r'C:\Users\admin\PycharmProjects\pythonProject\Pandas\data.csv',nrows=1)#nrows will be use to filter number of rows
print(df)




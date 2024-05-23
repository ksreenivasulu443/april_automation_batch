import numpy as np
import pandas as pd
#order of data types
#bol<int<float<str
#arrays will store homoegeneous data
#using list type
arr=np.array([1,2,3,'sreee'])
print('type of arr',type(arr))
print('value of arr[0] and its type',arr[3],type(arr[3]))
#using tuple type
arr2=np.array((1,2,3,'sreee'))
print('type of arr2',type(arr2))
print('value of arr[0] and its type',arr2[3],type(arr2[3]))
# 2dimensional array
arr3=np.array([[1,2,3,'sreee'],[4,5,6,7]])
print('type of arr3',type(arr3))
print('value of arr3[[0][0]] and its type',arr3[0][0],type(arr3[0][0]))
#comparision between array and list
ls=[1,2,3,'sree']
print('type of arr',type(ls))
print('value of ls[0] and its type',ls[3],type(ls[3]))

#numpy series
series=pd.Series([1,2,3,4],index=['a','b','c','d'])
print('type of arr',type(series))
print('value of series[a] and its type',series['a'],type(series['a']))
print('type of data in series',series.dtypes)
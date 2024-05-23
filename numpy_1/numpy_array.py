import numpy as np

import pandas as pd

# bool<int<float<str
# list,tuple, array

arr = np.array([[1,2,3,10.3,'sreeni'],[1,2,3,4,5]])
print("type of arr", type(arr))
print("value of arr[0][0] and type of arr[0][0]", arr[0][4], type(arr[0][4]))
# print("value of arr[1] and type of arr[1]", arr[1], type(arr[1]))
# print("value of arr[2] and type of arr[2]", arr[2], type(arr[2]))
# print("value of arr[3] and type of arr[3]", arr[3], type(arr[3]))


ls = [1,2,3,10.2]
print("type of ls", type(ls))
print("value of ls[0] and type of ls[0]", ls[0], type(ls[0]))
print("value of ls[1] and type of ls[1]", ls[1], type(ls[1]))
print("value of ls[2] and type of ls[2]", ls[2], type(ls[2]))
print("value of ls[0] and type of ls[3]", ls[3], type(ls[3]))

series = pd.Series([1, 2, 3, 4.0,'str'], index=['a','b','c','d','e'])

print("type of series",type(series))

print(series['b'])

print("type of data in series", series.dtypes)

print("all methods available", dir(series))

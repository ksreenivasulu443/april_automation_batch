import numpy as np
import pandas as pd


arr = np.array([[1, 2, 3, 4, "Ram", 1+8j],[1, 2, 3, 4, 5, 6]])
print("type of arr is", type(arr))
print("vale of arr[0] and type of arr[0]", arr[1][5], type(arr[1][5]))


series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

print("type of series is", type(series))
print("value of b index", series['b'])
print("type of data in series", series.dtypes)
print("all methods available", dir(series))

arr1 = np.array([[1, 2, 3, 4, 5],['Ajay', 'Baskar', 'Chandan', 'Deva', 'Esha']])
print("type of arr is", type(arr1))
print("vale of arr[0] and type of arr[0]", arr1[1][2], type(arr1[1][2]))
print("vale of arr1", arr1)



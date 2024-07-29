import numpy as np
import pandas as pd
# boolean<int<float<str here the priority of datatype when run the arry , high priority is string


# arr = np.array([1, 2, 3, 10, 'lina'])
# print("type of arr", type(arr))
# print("value of arr[0] and type of arr[0]", arr[0], type(arr[0]))
# print("value of arr[1] and type of arr[1]", arr[1], type(arr[1]))
# print("value of arr[2] and type of arr[2]", arr[2], type(arr[2]))
# print("value of arr[3] and type of arr[3]", arr[3], type(arr[3]))
# print("value of arr[4] and type of arr[4], ", arr[4],type(arr[4]))
arr = np.array([[1, 2, 3, 5], [3, 4, 5, 6]])
print("type of arr", type(arr))
print("value of arr[0][0] and type of arr[0][0]",arr[0][0], type(arr[0][0]))


ls = [1, 2, 3, 10, 'lina']
print("type of ls", type(ls))
print("value of ls[0] and type of ls[0]", ls[0], type(ls[0]))
print("value of ls[1] and type of ls[1]", ls[1], type(ls[1]))
print("value of ls[2] and type of ls[2]", ls[2], type(ls[2]))
print("value of ls[3] and type of ls[3]", ls[3], type(ls[3]))
print("value of ls[4] and type of ls[4]", ls[4], type(ls[4]))

series = pd.series([1, 2, 3, 5], index=['a','b', 'c','d'])
print("type of series",type(series))




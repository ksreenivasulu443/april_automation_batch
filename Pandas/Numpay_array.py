# import numpy as np
#
#import pandas as pd
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


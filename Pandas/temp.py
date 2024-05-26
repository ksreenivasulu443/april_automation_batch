import numpy as np
import pandas as pd

# arr=np.array([1,2,3,7.0])
# print("type of arr is:",type(arr))
# print("value of arr[0] and type of arr[0]",arr[0],type(arr[0]))
# print("value of arr[1] and type of arr[1]",arr[1],type(arr[1]))
# print("value of arr[2] and type of arr[2]",arr[2],type(arr[2]))
#
#
# series = pd.Series([1,2,3,4],index=['a','b','c','d'])
# print(series)
#
# print("all methods avaliable in data frames",dir(series))

import pyDataProfiling
from ydata_profiling import ProfileReport

df = pd.read_csv(r'C:\Users\mahab\PycharmProjects\april_automation_batch\Files\IPL Ball-by-Ball 2008-2020.csv')

profile = ProfileReport(df)

profile.to_file(r'C:\Users\mahab\PycharmProjects\april_automation_batch\Files\abc2.xlsx')
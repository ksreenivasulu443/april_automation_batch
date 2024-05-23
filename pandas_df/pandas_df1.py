import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

print("type of data", type(data))
df = pd.DataFrame(data)
print(df)
# print(help(pd.DataFrame))
df2 = pd.DataFrame([11,12,13,14,15], columns=['sno'], index=['a','b','c','d','e'])
print(df2)
ser = pd.Series([1, 2, 3], index=["a", "b", "c"])
df = pd.DataFrame(data=ser)
print("series converted as df")
print(df)

#
# df = pd.DataFrame(data= data(list, tuple, dict, series, arrays), columns=[columns], index=, dtype=)

# print(help(pd.read_csv))

df = pd.read_csv(filepath_or_buffer='/Users/harish/PycharmProjects/april_automation_batch/FIles/Contact_info.csv')

print(df)
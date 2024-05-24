import pandas as pd
from pandasql import sqldf

# from python_function.function_part1 import calc

# data = {'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35],
#         'City': ['New York', 'Los Angeles', 'Chicago']}
#
# print("type of data", type(data))
# df = pd.DataFrame(data)
# print(df)
# # print(help(pd.DataFrame))
# df2 = pd.DataFrame([11,12,13,14,15], columns=['sno'], index=['a','b','c','d','e'])
# print(df2)
# ser = pd.Series([1, 2, 3], index=["a", "b", "c"])
# df = pd.DataFrame(data=ser)
# print("series converted as df")
# print(df)

#
# df = pd.DataFrame(data= data(list, tuple, dict, series, arrays), columns=[columns], index=, dtype=)

# print(help(pd.read_csv))

print("reading csv files")
source = pd.read_csv(filepath_or_buffer='/Users/harish/PycharmProjects/april_automation_batch/FIles/Contact_info.csv', nrows=1000)
target = pd.read_csv(filepath_or_buffer='/Users/harish/PycharmProjects/april_automation_batch/FIles/Contact_info_t.csv', nrows=10)
print(source)

# print("read parquet files")

# source_par = pd.read_parquet("/Users/harish/PycharmProjects/april_automation_batch/FIles/userdata1.parquet")
# print(source_par)
# print("read excel file")
# source_excel = pd.read_excel("/Users/harish/PycharmProjects/april_automation_batch/FIles/Master_Test_Template.xlsx")
# print(source_excel)
#
# print(sqldf('''select col1, col2 from source where
#                     Identifier =1 or  Surname = 'Kattubadi'
#                     '''))
#
# print(sqldf("""select * from source except select * from target"""))

# print("top n record")
# print(source.head(4))
# print("bottom n record")
# print(source.tail(4))
#
# print("describe data")
# print(source.describe())
#
# print("selecting Identifier column data")
# print(source['Phone'])
# print(type(source['Phone']))
# print("selecting two columns data")
# print(source[['Identifier', 'Phone','birthmonth']])
# print(type(source[['Identifier', 'Phone','birthmonth']]))
#
# print("all the  columns")
# print(source.columns)
# print(" all column names with datatype")
# print(source.dtypes)

# Selecting rows by index
print(source.iloc[0:3, 4:9])  # First row
# source.iloc[0:2, 0:2]  # First two rows

print(source.loc[0:3,'Identifier':'city' ])


print(source[(source.Identifier > 5) & (source.Surname=='Arun')])







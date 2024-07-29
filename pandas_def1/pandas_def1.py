import pandas as pd

from pandasql import sqldf

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 39],
        'City': ['New York', 'los Angeles', 'chicago']}
print('type of data', type(data))
df = pd.DataFrame(data)
print(df)

# print(help(pd.DataFrame))
df2 = pd.DataFrame([1, 2, 3, 4, 5], columns=['sno'])
print(df2)

# ser = pd.series([1, 2, 3], index=["a", "b", "c"])
# df = pd.DataFrame(data=ser)
# print("series converted as df", df)
# syntax of data fa
#df = pd.DataFrame(data= data(list, touple, dict, array, series), columns['columns'],index=, datatype=)
# print(help(pd.read_csv))
source = pd.read_csv(
    filepath_or_buffer=r'C:\Users\hp\PycharmProjects\april_automation_batch_lina\FIles\Contact_info.csv')
print(source)

# target = pd.read_csv(
#     filepath_or_buffer=r'C:\Users\hp\PycharmProjects\april_automation_batch_lina\FIles\Contact_info_t.csv', nrows=10)
# print(target)
#
# df_par = pd.read_parquet(r"C:\Users\hp\PycharmProjects\april_automation_batch_lina\FIles\userdata1.parquet")
# print(df_par)
#
# source_exl = pd.read_excel(r"C:\Users\hp\PycharmProjects\april_automation_batch_lina\FIles\Master_Test_Template.xlsx",
#                            nrows=20)
# print(source_exl)
# print(sqldf('''select * from source
#                       where identifier = 1 or Surname='Kattubadi'
#                       '''))
# print(sqldf('''select * from source except select * from target'''))
print('top n records')
print(source.head(4))
print('bottom n records')
print(source.tail(4))
print('describe n records')
print(source.describe())
print("selecting  Phone column data")
print(source['Phone'])
print(type(source['Phone']))
print("selecting identifier and Phone columns data")
print(source[['Identifier', 'Phone']])
print(type(source[['Identifier', 'Phone']]))
print('all columns in table')
print(source.columns) # its show all columns in table in list
print('display datatype of all columns')
print(source.dtypes) #its show datatype of all columns in table


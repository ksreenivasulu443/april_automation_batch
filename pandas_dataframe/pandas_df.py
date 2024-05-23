#
# import pandas as pd
# data = {'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35],
#         'City': ['New York', 'Los Angeles', 'Chicago']}
# df = pd.DataFrame(data)
# print(df)
#
# print(type(data))
#
# print(help(pd.DataFrame(data)))
#
# df2=pd.DataFrame([11,12,13,14,25],columns=['sno'], index=['a','b','c','d','e'])
# print(df2)
# print(help(pd.DataFrame))

import pandas as pd

csv_read_df=pd.read_csv(r'C:\Users\bbhoi\PycharmProjects\datapythonautomation\Files\Contact_info.csv')
print(csv_read_df)



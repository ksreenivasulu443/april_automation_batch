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

# import pandas as pd
# df2=pd.DataFrame([11,12,13,14,25])
# print(df2)

# import pandas as pd
# df2=pd.DataFrame([11,12,13,14,25],columns=['sno'])
# print(df2)

# import pandas as pd
# df2=pd.DataFrame([11,12,13,14,25],columns=['sno'], index=['a','b','c','d','e'])
# print(df2)

# print(help(pd.DataFrame))


#


# from pandasql import sqldf

# import pandas as pd
# csv_read_df=pd.read_csv(r'C:\Users\bbhoi\PycharmProjects\datapythonautomation\Files\Contact_info.csv',nrows=5)
# print(csv_read_df)
#
# import pandas as pd
# source_csv=pd.read_csv(r'C:\Users\bbhoi\PycharmProjects\datapythonautomation\Files\Contact_info.csv',nrows=5)
#
# import pandas as pd
# target_csv=pd.read_csv(r'C:\Users\bbhoi\PycharmProjects\datapythonautomation\Files\Contact_info_t.csv',nrows=5)

# print(source_csv.dtypes)
# print(source_csv[0:2])

#
# import pandas as pd
# source_par=pd.read_parquet(r'C:\Users\bbhoi\PycharmProjects\datapythonautomation\Files\userdata1.parquet')
# print(source_par)
#
# import pandas as pd
# source_excel=pd.read_excel(r'C:\Users\bbhoi\PycharmProjects\datapythonautomation\Files\Master_Test_Template.xlsx')
# print(source_excel)

import pandas as pd
from pandasql import sqldf
# print(sqldf("select * from source_csv where identifier=1"))
# print(source_csv.columns)
# print(list(source_csv.iterrows()))
#
# print(sqldf("select * from source_csv except select * from target_csv"))
# print(sqldf("select * from target_csv except select * from source_csv"))

# df=pd.DataFrame(data=data(list,tuple,dict,Series,arrays),columns=[columns],index=,dtype=)
#
# print(source_csv.count())
# print(source_csv.head(1))
# print(source_csv.tail(1))
# print(source_csv.describe())

# print((source_csv['Identifier']))
# print(sqldf("select Identifier from source_csv"))
# print(type(source_csv['Identifier']))
#
# import pandas as pd
# print((source_csv[['Identifier','Phone']]))
# print(sqldf("select Identifier,Phone from source_csv"))
# print(type(source_csv[['Identifier','Phone']]))

# print(source_csv.iloc[0])
# print(source_csv.iloc[2:4,1:6])
# print(source_csv.loc[2:4,'Identifier':'city'])

# doubt
# print(source_csv[source_csv['Identifier']>5 & (source_csv['surname'] like 'H%')])
# print(source_csv[(source_csv.Identifier]>5) & (source_csv.surname like 'H%']))
# print(source_csv[(source_csv.Identifier>5) & (source_csv.surname like 'H%')])

-----Data Profiling------

# from ydata_profiling import ProfileReport
#
# df=pd.read_csv(r'C:\Users\bbhoi\PycharmProjects\datapythonautomation\Files\Contact_info.csv')
#
# profile=ProfileReport(df)
#
# profile.to_file(r'C:\Users\bbhoi\PycharmProjects\datapythonautomation\Files\out.html')
#

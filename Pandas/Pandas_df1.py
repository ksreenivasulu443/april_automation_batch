import pandas as pd
from pandasql import sqldf

# data={'name':['Bob','James','Steve','Rob'],'Age' : [20, 30, 40,25] ,
#              'city' : ['Ban','Hyd','Pune','Delhi']}
# df=pd.DataFrame(data)
# print(df)

# df2=pd.DataFrame([11,12,13,14],columns=['sno'],index=['a','b','c','d'])
# print(df2)

# df=pd.read_csv(filepath_or_buffer=r'C:\Users\mahab\PycharmProjects\april_automation_batch\Files\Contact_info.csv')
# print(df)

#
# print("read parquet file")
# source_parquet=pd.read_parquet(r'C:\Users\mahab\PycharmProjects\april_automation_batch\Files\userdata1.parquet')
# print(source_parquet)
#
# print("read csv file")
# source_csv=pd.read_csv(r'C:\Users\mahab\PycharmProjects\april_automation_batch\Files\template.csv')
# print(source_csv)
#
# print("read excel file")
# source_excel=pd.read_excel(r'C:\Users\mahab\PycharmProjects\april_automation_batch\Files\Master_Test_Template.xlsx')
# print(source_excel)

source = pd.read_csv(r'C:\Users\mahab\PycharmProjects\april_automation_batch\Files\Contact_info.csv', nrows=1000)
target = pd.read_csv(r'C:\Users\mahab\PycharmProjects\april_automation_batch\Files\Contact_info_t.csv', nrows=10)
#
#print(sqldf('select * from source except select * from target'))
#
# print(sqldf('select * from source where identifier=2 or Phone=8765656555'))

#print(sqldf('select * from source where identifier between 2 and 5'))
# print("first row records")
# print(source.head())
#
# print("last row records")
# print(source.tail())
#
#selecting single identifier
# print(source.describe())
#print(source[['Identifier']])
#selecting 2 columns
#print(source[['Identifier','Phone']])

#print(source.iloc[0:1])
#display index values
# print(source.iloc[4:10  ,0:3])

#print(source.iloc[:,0:7])

#print(source.loc[0:3,'Surname' : 'primary_street_name'])

# source['Salary']=[1000,2000,3000]
# print(source)




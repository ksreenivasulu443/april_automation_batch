#source_par = pd.read_parquet (""
# print(source_par)read_excel("")
#source_excel pd.read_excel("

from pandasql import sqldf # pandassql is the package
import  pandas as pd #panda is library
df = pd.read_csv(filepath_or_buffer=r'C:\Users\admin\PycharmProjects\pythonProject\Pandas\data.csv',nrows=1)#nrows will be use to filter number of rows
print(df)

from pandasql import sqldf
# pandassql is the package

#print(sqldf("""select * from source except select * from target"""))
#print(sqldf('''select * from source where id =1'''))
#print("top n record")
#print("source.head(4)")
#print("bottom n record")
#print("source.tail(4)")
#print("describe data")
#print("source.describe()") it will give count og records, min max values in table
#print("source['id'])#it will fetch column from table
#print("source[['id','name']])
#print("all column")
#print(source.column) it will display all columns
#print("all columns and data types")
#print(source.dtype)

#iloc:
#selecting the rows by index
#print(source.iloc[0:2] )it will fetch one row
#print(source.iloc[4:6]) it will fetch 4, 5 rows

##print(source.iloc[4:6,2:8])It will fetch 4 to 5 rows and 2 to 7 columns

#Loc:
#print(souce.loc[0:3,'id':city) it will print 0,1,2,3 rows and id column to city column

#print(source[(source['id']>5) & (source['name']=='sham')])

#####################################################################################3
#To know the insights of requirement for source table (duplicates,max,count etc....)

from ydata_profiling import ProfilingReport
#df = pd.read.csv(r'C:\Users\admin\PycharmProjects\pythonProject\Pandas\data.csv')

#profile = ProfileReport(df)

#profile.to_file(r'C:\Users\admin\PycharmProjects\pythonProject\Pandas\data.html')

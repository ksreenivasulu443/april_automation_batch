import pandas as pd
from ydata_profiling import ProfileReport


source = pd.read_csv('D:/ETL_Automation/emp1.csv')
target = pd.read_csv('D:/ETL_Automation/emp2.csv')

df_parquet = pd.read_parquet(r"D:\ETL_Automation\ReadFiles\userdata1.parquet", engine='pyarrow')
# print(df_parquet)

df_csv = pd.read_csv(r"D:\ETL_Automation\ReadFiles\Contact_info.csv")

profile = ProfileReport(df_csv)

profile.to_file(r"C:\Users\User\PycharmProjects\pyspark\Arpril_automation_python\Files\out.html")


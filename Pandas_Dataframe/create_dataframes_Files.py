import pandas as pd
df_csv=pd.read_csv
# print(help(pd.read_csv))
# df = pd.DataFrame(data= data(list, tuple, dict, series, arrays), columns=[columns], index=, dtype=)

# print(help(pd.read_csv))

df = pd.read_csv(filepath_or_buffer=r'D:\Back up\Automation\Contact_info.csv')

print(df)
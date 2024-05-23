import pandas as pd
from sqlite4 import SQLite4
from sqlite3 import connect


conn = connect(':memory:')
data = {'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
print(df)
df.to_sql(name='test_data', con=conn)
cnt = pd.read_sql('SELECT count(*) FROM test_data', conn)
rec = pd.read_sql('SELECT * FROM test_data', conn)
print(cnt)
print(rec)

df2 = pd.DataFrame( ([1, "Arun", 'B+'],[2, "Babu", 'A'],[3, "Chiru", 'B+']),
                    columns=[ "sno", "Student_name", "Grade"], index=['a','b','c'])
print(df2)

# print(help(pd.DataFrame))

ser = pd.Series([1, 2, 3], index=["a", "b", "c"])
df3 = pd.DataFrame(data=ser)
print("series converted as df")
print(df3)
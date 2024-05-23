import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)
df2=pd.DataFrame([11,12,13,14,15],columns=['sno'],index=['a','b','c','d','e'])

print(df2)
series=pd.Series([20,30,40,50,60],)
df=pd.DataFrame(data=series)
print(df)




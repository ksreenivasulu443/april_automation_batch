import pandas as pd
from sqlite3 import connect


conn = connect(':memory:')


def read_fun(path):
    print("i am reading data from :", path)
    a = pd.read_csv(path)
    return a


source = read_fun('D:/ETL_Automation/emp1.csv')
target = read_fun('D:/ETL_Automation/emp2.csv')


def count_check(source, target):
    source.to_sql(name='emp1', con=conn)
    target.to_sql(name='emp2', con=conn)
    ls=[]
    lt=[]
    cnt = pd.read_sql('SELECT count(*) FROM emp1', conn)
    rec = pd.read_sql('SELECT count(*) FROM emp2', conn)
    for i in cnt:
        ls.append(cnt)
    print(ls)
    scr_cnt = print("scr_cnt",cnt)
    trg_cnt = print("trg_cnt", rec)
    if scr_cnt == trg_cnt:
        print(f"count is matching: source count is {scr_cnt} and target count is {trg_cnt}")
    return (f"count is matching: source count is {scr_cnt} and target count is {trg_cnt}"), scr_cnt == trg_cnt


print(count_check(source, target))




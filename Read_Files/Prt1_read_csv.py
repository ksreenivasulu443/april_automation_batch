import pandas as pd
from sqlite3 import connect

from pandasql import sqldf

conn = connect(':memory:')


# def read_fun(path):
#     print("i am reading data from :", path)
#     a = pd.read_csv(path)
#     return a
#
#
# source = read_fun('D:/ETL_Automation/emp1.csv')
# target = read_fun('D:/ETL_Automation/emp2.csv')


# def count_check(source, target):
#     source.to_sql(name='emp1', con=conn)
#     target.to_sql(name='emp2', con=conn)
#     ls=[]
#     lt=[]
#     cnt = pd.read_sql('SELECT count(*) FROM emp1', conn)
#     rec = pd.read_sql('SELECT count(*) FROM emp2', conn)
#     for i in cnt:
#         ls.append(cnt)
#     print(ls)
#     scr_cnt = print("source_count is ", cnt)
#     trg_cnt = print("Target_count is ", rec)
#     if scr_cnt == trg_cnt:
#         print(f"count is matching: source count is {scr_cnt} and target count is {trg_cnt}")
#     return (f"count is matching: source count is {scr_cnt} and target count is {trg_cnt}"), scr_cnt == trg_cnt
#
#
# print(count_check(source, target))

def data_ch(source, target):
    Mismatch_S_T = sqldf("select * from source except select * from target")
    Mismatch_T_S = sqldf("select * from target except select * from source")
    print("s-t", Mismatch_S_T)
    print("t-s", Mismatch_T_S)


def cnt_ch(source, target):
    scr_cnt = source.shape[0]
    trg_cnt = target.shape[0]
    if scr_cnt==trg_cnt:
        print(f"Source count is {scr_cnt} matches with Target count is {trg_cnt}")
    else:
        print("Source count not matches with Target count and count difference is", scr_cnt - trg_cnt)


def dupl_ch(target, keycolumn):
    sql = f'''select {keycolumn} from target group by {keycolumn} having count(*)>1'''
    duplicate = sqldf(sql)
    if duplicate.shape[0]>0:
        print("Duplicates")
    else:
        print("No Duplicate")

# print(cnt_ch(source, target))
# print(dupl_ch(target, 'EMPNO'))


# testcases = pd.read_excel(r"D:\ETL_Automation\ReadFiles\File_Path.xlsx")
# for index, row in testcases.iterrows():
#     # print("index value is", index)
#     # print("row value is", row['source_file'])
#     # print("row value is", row['target_file'])
#     # print("row value is", row['key_column'])
#     source_path = row["source_file"]
#     target_path = row["target_file"]
#     source = pd.read_csv(source_path)
#     target = pd.read_csv(target_path)
#     cnt_ch(source, target)
#     dupl_ch(target, row['key_column'])
#     data_ch(source, target)

def read_fun(path):
    testcases = pd.read_excel(path)
    for index, row in testcases.iterrows():
        # print("index value is", index)
        # print("row value is", row['source_file'])
        # print("row value is", row['target_file'])
        # print("row value is", row['key_column'])
        source_path = row["source_file"]
        target_path = row["target_file"]
        source = pd.read_csv(source_path)
        target = pd.read_csv(target_path)
        cnt_ch(source, target)
        dupl_ch(target, row['key_column'])
        data_ch(source, target)

read_fun(r"D:\ETL_Automation\ReadFiles\File_Path.xlsx")
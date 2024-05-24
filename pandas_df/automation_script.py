from pandasql import sqldf
import pandas as pd


def count_val(source, target):
    #src_cnt = sqldf("select count(*) count1 from source")
    src_cnt = source.shape[0]
    tgt_cnt = target.shape[0]
    #tgt_cnt = sqldf("select count(*) count1 from target")
    if src_cnt == tgt_cnt:
        print("matching")
    else:
        print("count validation failed", src_cnt - tgt_cnt)



def Column_value_val(source, target):
    Mismatch_S_T = sqldf("select *  from source except select *  from target")
    Mismatch_T_S = sqldf("select *  from target except select *  from source")
    print("Mismatch records between source and target")
    print(Mismatch_S_T)
    print("Mismatch records between target and source")
    print(Mismatch_T_S)
    #source.compare(target)



# Column_value_val(source, target )

def duplicate(target, key_column):
    sql = f'''select {key_column}, count(*)  from target group by {key_column} having count(*)>1'''
    duplicate = sqldf(sql)
    if duplicate.shape[0] > 0:
        print("duplicates")
    else:
        print("no duplicates")

test_cases =  pd.read_csv("/Users/harish/PycharmProjects/april_automation_batch/FIles/template.csv")
print(test_cases)
for index,row in test_cases.iterrows():
    source_path = row['source_file']
    target_path = row['target_file']
    target = pd.read_csv(target_path)
    source = pd.read_csv(source_path)
    count_val(source, target)
    Column_value_val(source,target)

import pandas as pd

import numpy as np

# np.random.randn(1,20)

from ydata_profiling import ProfileReport
df = pd.read_csv(r"/Users/harish/PycharmProjects/april_automation_batch/FIles/Contact_info.csv")

profile = ProfileReport(df)

#profile.to_html()


profile.to_file(r"/Users/harish/PycharmProjects/april_automation_batch/FIles/out.html")


import pandas as pd


def read_fun(path):
    print("i am reading data from :", path)
    a = pd.read_csv(path)
    return a

source = read_fun('D:/ETL_Automation/emp1.csv')
print(type(source))
print(source.head(3))
target = read_fun('D:/ETL_Automation/emp2.csv')
print(target.head(3))

def count_check(source, target):
    source_count = source.shape[0]
    target_count = target.shape[0]
    if source_count == target_count:
        print(f"count is matching: source count is {source_count} and target count is {target_count}")
    else:
        print(f"count is not matching:  source count is {source_count}, target count is {target_count} and difference "
              f"is {source_count-target_count}")


count_check(source, target)

def data_compare(source, target):
    return source.compare(target)

print(data_compare(source, target))

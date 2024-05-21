import pandas as pd
def read_fun(path, file_type):
    print("i am reading data from :", path)
    if file_type=='csv':
        df = pd.read_csv(path)
    elif file_type =='excel':
        df= pd.read_excel(path)
    return df


source = read_fun(r'D:\Back up\Automation\source.csv','csv')
print(type(source))
print(source.head(3))
target = read_fun(r'D:\Back up\Automation\target.xlsx','excel')
print(type(target))
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
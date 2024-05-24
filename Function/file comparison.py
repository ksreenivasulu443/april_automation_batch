import pandas as pd

pd.DataFrame


def read_fun(path):
    print("i am reading data from:", path)
    df = pd.read_csv(path)
    return df


source = read_fun(r"C:\Users\mahab\PycharmProjects\april_automation_batch\Function\source.csv")
print(source.head(3))
target = read_fun(r"C:\Users\mahab\PycharmProjects\april_automation_batch\Function\target.csv")
print(target.head(3))


def count_check(source, target):
    source_count = source.shape[0]
    target_count = target.shape[0]
    if source_count == target_count:
        print(f"count is matching with {source_count} and {target_count}")
    else:
        print(f"count is not matching with {source_count} and {target_count} and abs({source_count}-{target_count})")


count_check(source, target)


def data_compare(source, target):
    return source.compare(target)


print(data_compare(source, target))

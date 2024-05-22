import pandas as pd

def read_file(path,type):
    try:
        if type == 'csv':
            df = pd.read_csv(path)
            print(df.head(2))

        elif type =='excel':
            df = pd.read_excel(path)
            print(df.head(2))
        elif type =='text':
            df = pd.read_csv(path, delimiter=',')
            print(df.head(2))
        return df


    except FileNotFoundError as e:
        print("default error", e)
        return None

source = read_file("exceptions/source1.csv",'csv')
target = read_file("exceptions/target.txt",'text')

def compare(s,t):
    print("matching")

compare(source, target)

# def read_file(path,type):
#         if type == 'csv':
#             df = pd.read_csv(path)
#             print(df.head(2))
#
#         elif type =='excel':
#             df = pd.read_excel(path)
#             print(df.head(2))
#         elif type =='text':
#             df = pd.read_test(path)
#             print(df.head(2))
#         return df
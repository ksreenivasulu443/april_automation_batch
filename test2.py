import builtins

# # # # ls = []
# # # # print("type of ls ", type(ls))
# # # # print("id(ls)", id(ls))
# # # #
# # # # ls2 = list()
# # # #
# # # # print("type of ls2 ", type(ls2))
# # # #
# # # # ls.append(1)
# # # # print(ls)
# # # #
# # # # ls.append([1,2])
# # # #
# # # # print(ls)
# # # #
# # # # ls.extend([1,2,3])
# # # # print(ls)
# # # #
# # # # print("id(ls)", id(ls))
# # #
# # # import sys
# # #
# # # # Create an empty list
# # # my_list = []
# # #
# # # # Print the size of the list object
# # # print("Size of empty list:", sys.getsizeof(my_list))
# # #
# # # # Append elements to the list
# # # for i in range(10):
# # #     my_list.append(i)
# # #
# # # # Print the size of the list object after appending elements
# # # print("Size of list with 10 elements:", sys.getsizeof(my_list))
# # #
# # # # Print the length and capacity of the list
# # # print("Length of list:", len(my_list))
# # # print("Capacity of list:", my_list.__sizeof__())
# # #
# # # import sys
# # #
# # # # Create an empty tuple
# # # my_tuple = ()
# # #
# # # # Print the size of the tuple object
# # # print("Size of empty tuple:", sys.getsizeof(my_tuple))
# # #
# # # # Create a tuple with elements
# # # my_tuple = (1, 2, 3, 4, 5,6,7,8,9,10)
# # #
# # # # Print the size of the tuple object with elements
# # # print("Size of tuple with elements:", sys.getsizeof(my_tuple))
# # #
# # # a=10
# # # print("Size of a with elements:", sys.getsizeof(a))
# # #
# # # # Print the length of the tuple
# # # print("Length of tuple:", len(my_tuple))
# # #
# # # print("Capacity of my_tuple:", my_tuple.__sizeof__())
# # #
# # # ls2 =[1,23,3]
# # # ls3 = ls2
# # #
# # # print("ls3", ls3)
# # # print("ls2", ls2)
# # #
# # # ls2.append(1)
# # #
# # # print("ls3", ls3)
# # # print("ls2", ls2)
# # #
# # # ls4 = ls2.copy()
# # # ls4.append(5)
# # #
# # # print("ls3", ls2)
# # # print("ls2", ls4)
# # #
# # # #ls5 = ls2.shallo
# # #
# # # print(ls2.index(3))
# # #
# # # ls2.insert(10,8)
# # #
# # # print("ls2", ls2)
# # #
# # # ls2.pop()
# # #
# # # print(ls2)
# # # ls2.pop()
# # # print(ls2)
# # #
# # # ls2.remove(23)
# # # print(ls2)
# # #
# # # ls2.extend([1,2,3,4,4,8,19,20,212,212,45,2,3])
# # #
# # # print(ls2)
# # #
# # # ls2.reverse()
# # #
# # # print(ls2)
# # #
# # # ls2.reverse()
# # #
# # # ls= [1,4,2,7,4,2,8]
# # # ls.sort(reverse=True)
# # #
# # # print(ls)
# # #
# # # ls.reverse()
# # #
# # # print(ls)
# # #
# #
# # # import gc
# # #
# # # a = 1002
# # # referrers = gc.get_referrers(a)
# # #
# print("Number of references to 'a':", len(referrers))
# print("References to 'a':")
# for referrer in referrers:
#     print(referrer)
# #
# #
# # import time
# #
# # # Create a list with 10 million elements
# # my_list = list(range(10000000))
# #
# # # Measure the time taken to access an element by index
# # start_time = time.time()
# # element = my_list[5000000]
# # end_time = time.time()
# # print("Time taken to access an element in a list:", end_time - start_time, "seconds")
# #
# #
# # import time
# #
# # # Create a tuple with 10 million elements
# # my_tuple = tuple(range(10000000))
# #
# # # Measure the time taken to access an element by index
# # start_time = time.time()
# # element = my_tuple[5000000]
# # end_time = time.time()
# # print("Time taken to access an element in a tuple:", end_time - start_time, "seconds")
# #
# # import time
# #
# # # Create a dictionary with 10 million key-value pairs
# # my_dict = {i: i for i in range(10000000)}
# #
# # # Measure the time taken to access a value by key
# # start_time = time.time()
# # value = my_dict[5000000]
# # end_time = time.time()
# # print("Time taken to access a value in a dictionary:", end_time - start_time, "seconds")
# #
# # seconds
#
# # ls =[1,2,3,4]
# # ls2=[1,2,3]
# #
# # ls3 = ls+ls2
# #
# # print(ls3)
# #
# # ls.append(5)
# #
# # print(ls3)
# #
# # ls4 = ls*2
# #
# # print(ls4)
# #
# # print([i*i for i in range(1,10)])
#
# dict = {}
#
# print(type(dict))
#
# dict2 = {1, 2, 3, 3}
#
# print(type(dict2))
#
# print(dir(dict))
#
# dict[1] = 'srreni'
# dict[2] = 'Hari'
#
# print(dict)
#
# print(dict.get(1))
# print(dict[1])
#
# print("keys", dict.keys())
#
# print("items", dict.items())
#
# x = ('key1', 'key2', 'key3')
# y = (3, 4, 5)
#
# thisdict = dict.fromkeys(x, y)
#
# print(thisdict)
#
# dict = {1: 'sreeni', 2: 'prakash'}
#
# print(dict)
# dict.update({1: 'Hari', 4: 'Harekrishna'})
# print(dict)

# aTuple = (1, 'Jhon', 1+3j)
# print(type(aTuple[2:3]))
#
#
#
# print(type(range(5))


# cott/tiger@host.docker.internal:1521/freepdb1

#
# import cx_Oracle
#
# # Create a table in Oracle database
# try:
#
#     con = cx_Oracle.connect('scott/tiger@localhost')
#     print(con.version)
#
#     # Now execute the sqlquery
#     cursor = con.cursor()
#
#     # Creating a table employee
#     cursor.execute(
#         "create table employee(empid integer primary key, name varchar2(30), salary number(10, 2))")
#
#     print("Table Created successfully")
#
# except:
#     print("There is a problem with Oracle")

# a = 5
#
# print(a==5)
# print(a!=5)
# print(a>5)
# print(a<5)
# print(a>=5)
# print(a<=5)
#
# source_count = 10
#
# target_count = 10
#
# print("source_count == target_count",source_count == target_count)
#
#
#
# if source_count>0 and target_count>0:
#     print("Data available for validation, proceed")
#
# x = 10
# y = 20
# z = x
#
# print(id(x))
# print(id(y))
#
# print(x is y)  # Output: False (x and y are two different lists)
# print(x is z)  # Output: True (x and z refer to the same list)
#
# print(x is not y)  #
# print(x is not z)  #

# x = 10
#
# if 10:
#     print("x is positive")

# num = 10
#
# # check and print type of num variable
# print("Type of variable before conversion : ", type(num))
#
# # convert the num into string
# converted_num = str(num)
#
# # check and print type converted_num variable
# print("Type After conversion : ",type(converted_num))

# print("gobals", globals())
#
# a= 10
#
# print("gobals", globals())
#
# def cal(a,b):
#     b=20
#     print("locals",locals())
#     def add():
#         c=20
#         print("locals inside add", locals())
#         return c+b
#     add()
#     return a+b
# print("gobals", globals())
# add= cal(10,20)
# print("gobals", globals())

# len('xyz')
#
# print(len)
# print(ValueError)
# print(type)
#
#
# add = lambda a,b: a+b
#
# print(add(4,5))
#
# convert_cols_lower = lambda col : col.lower()
#
# print(convert_cols_lower('Name'))
#
# cols= ['Full_Name','First_name','last_name','middle_name', 'Suffix_name','Phone']
#
# cols = map(convert_cols_lower,cols)
#
# print(list(cols))
#
# cols= ['Full_Name','First_name','last_name','middle_name', 'Suffix_name','Phone']
#
# select_name_columns = lambda col : col.lower().endswith('name')
#
# sel = filter(select_name_columns, cols)
#
# print(list(sel))
#
# var =11
# for j in range(2, 10, 1):
#         if var % 2 == 0:
#             print(var)
#             continue
#             var += 1
#             print(var)
#
# else:
#     print("for loop else")
# print(var)

# print("this is first line")
# print("this mid of code")
# try:
#     a= 1#int(input("enter a value:"))
#     b= 2#int(input("enter b value"))
#     print("value of a is", a)
#     print("value of b is ", b)
#     print("a and b multiplication", a*b)
#     print("div of a and b ", a/b)
#     print("c value is",c)
# # except ValueError as e:
# #     print("Hey some thing wrong..Check datatype",e)
# # except ZeroDivisionError as e:
# #     print("divisor is zero & Pls retry divisor non-zero value", e)
# # except NameError as e:
# #     print("name error, pls check variable definination", e)
#
# except (ValueError,ZeroDivisionError) as e:
#     print("Hey some thing wrong..Check datatype",e)
# except NameError as e:
#     print("name error, pls check variable definination", e)
#
# print("this is last line")
# ###Assertion##
# try:
#     assert 2 + 2 == 4
# except AssertionError as e:
#     print(f"AssertionError: {e}")
# ###Assertion##
#
# ###Attribute exception###
# str = 'sreeni'
# try:
#     str.UPPER()
# except AttributeError as e:
#     print(f"AttributeError: {e}")
# ###Attribute exception###
#
#
# import math
# try:
#     math.exp(1000)  # This would normally not raise FloatingPointError, but OverflowError
# except FloatingPointError as e:
#     print(f"FloatingPointError: {e}")
# except OverflowError as e:
#     print(f"OverflowError (in place of FloatingPointError): {e}")
#
#
# try:
#     import non_existent_module
# except ImportError as e:
#     print(f"ImportError: {e}")
#
#
# try:
#     my_list = [1, 2, 3]
#     print(my_list[5])
# except IndexError as e:
#     print(f"IndexError: {e}")
#
# try:
#     my_dict = {"name": "John"}
#     print(my_dict["age"])
# except KeyError as e:
#     print(f"KeyError: {e}")
#
# # import time
# # try:
# #     while True:
# #         time.sleep(1)
# # except KeyboardInterrupt:
# #     print("KeyboardInterrupt: Program interrupted by user")
#
#
# try:
#     x = [1] * (10**10)
# except MemoryError as e:
#     print(f"MemoryError: {e}")
#
# try:
#     print(unknown_variable)
# except NameError as e:
#     print(f"NameError: {e}")
#
#
#
#
# import os
# import io
#
# file_path = 'example.txt'
#
# try:
#     with open(file_path, 'r') as file:
#         content = file.read()
# except FileNotFoundError as e:
#     print(f"FileNotFoundError: {e}")
# except IsADirectoryError as e:
#     print(f"IsADirectoryError: {e}")
# except PermissionError as e:
#     print(f"PermissionError: {e}")
# except OSError as e:  # Catch-all for other OS-related errors
#     print(f"OSError: {e}")

import numpy as np

arr = np.array([[1, 2, '3', 4], [0, 1, 2, 3]])
print("type of arr", type(arr))
print(arr)

arr = np.array([1, 2, 4])
print("type of arr", type(arr))
print(type(arr[0]))
print(type(arr[1]))

sqrt_array = np.sqrt(arr)

print(sqrt_array)

random_normal = np.random.randn(3, 3)
print("random_normal", random_normal)

random_normal_custom = np.random.normal(5, 2, size=(3, 3))

print("random_normal_custom", random_normal_custom)

array = np.array([1, 2, 3, 4, 5])
random_choice = np.random.choice(array, size=1, replace=False)

print("random_choice", random_choice)

import pandas as pd

df = pd.read_csv("/Users/harish/Downloads/tested.csv")

print(df.head(2))

print(df.tail(2))

print(df.describe())

print(df.iloc[0:5, 2:4])

print(df.loc[0:4, 'Pclass':'Name'])

print(df[(df.Pclass == 3) & True])

print(df.count())

print(df.columns)

print(df.dtypes)

df.shape

from pandasql import sqldf

print(sqldf("select count(*) from df"))


def count_val(source, target):
    src_cnt = sqldf("select count(*) count1 from df")
    src_cnt = source.shape[0]
    tgt_cnt = target.shape[0]
    tgt_cnt = sqldf("select count(*) count1 from target")
    if list(src_cnt.count1) == list(tgt_cnt.count1):
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
    source.compare(target)


# Column_value_val(source, target )

def duplicate(target, key_column):
    duplicate = sqldf(f'''select {key_column}, count(*)  from target"
                       group by {key_column} having count(*)>1''')
    if duplicate.shape[0] > 0:
        print("duplicates")
    else:
        print("no duplicates")


df = pd.DataFrame(([1, 2, 3], [4, 5, 6]), columns=['sno', 'name', 'nam'])
print(df.head())


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


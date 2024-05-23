# # ***********LIST*********************
# A list in Python is a collection of items, separated by commas and enclosed within square brackets [ ] and Lists can contain elements of different data types, including numbers, strings, other lists, tuples, dictionaries, etc.
# Mutability: Lists are mutable, meaning you can change, add, and remove elements after the list has been created.
# Order: Lists maintain the order of elements as they are inserted.
# Elements: Indexing and Slicing: Elements in a list can be accessed using indices. Python also supports slicing, which allows you to extract a portion of the list.
# e.g., first_list = [1, 2, 'hello',1+2j,10.3]

# ls1=[1,2,3]
# ls2=[4,5,"6"]
# print("addition of two list:",ls1+ls2)
# ls3=["Data","Automation"]
# print("addition of three list:",ls1+ls2+ls3)

# list=[]
# print("blank list:",list)
#
# List = [10, 20, 14]
# print("\nList of numbers: ")
# print(List)
#
# List = ["ETL", "Data", "Engineering"]
# print("\nList Items: ")
# print("index0 value:",List[0])
# print("index1 value:",List[2])

# List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
# print("\nList with the use of Numbers: ")
# print(List)


# List = [1, 2, 'python', 4, 'For', 6, 'automation']
# print("\nList with the use of Mixed Values: ")
# print(List)


# list = [['python', 'for'], ['automation']]
# # print(list[0])
# # print(list[0][0])
# # print(list[0][1])
# # print(list[0][-1])
# # print(list[0][-2])
# # print(list[1])
# # print(list[::-1])
# print(list.reverse())


# List1 = []
# print(len(List1))
#
# List2 = [10, 20, 14]
# print(len(List2))
#

# string = input("Enter elements with space: ")
# list=string.split()
# print("string after split:",list)

# n=int(input("enter list size:"))
# list=list(map(int,input("enter integer:").strip().split()))[:n]
# print('The list is:', list)

# list=[]
# print(list)
#
# list.append(1)
# print(list)
# list.append(2)
# print(list)
# list.append(3)
# print(list)

# list=[]
# for i in range(1,5):
#     list.append(i)
# # print("list:")
# print(list)

# list=[1,2,3,4]
# print("initial list:",list)
# list.insert(3,12)
# print("list after insert:",list)
# list.insert(0,"elements")
# print(list)
#
# list=[5,6,7,8]
# list.extend([9,"element1","element2"])
# print("\nList after performing Extend Operation: ")
# print(list)
#
# list=[5,6,7,8]
# print(list.reverse())
#
# list=[5,6,7,8]
# print(list)
# print(list[::-1])


# duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# print(duplicates)
# no_duplicates=list(set(duplicates))
# print(no_duplicates)

# L = [True, "2", 3.0, 4]
# print(L)
# print(type(L))

# ls = [1, 2.0, True, 1+2j, 'string', (1,2),[3,4]]
# print(ls)
# print(type(ls))
# print(id(ls))
# print(ls[0])
# print(ls[-1])
#
# print(ls[0:4])
# print(ls[-4:-1])
#
# print(ls[0:4:1])
# print(ls[0:4:2])
#
# ls1=[1,2,3,4,5,6,7,8,9]
# print(ls1)

# my_list = [1, 2, 3]
# my_list.append('apple')
# my_list.append([5, 6, 7])  # Appending a list as an element
# print(my_list)
# ####################################APPEND()########################
# ls1=[]
# ls1.append(5)
# print(ls1)
#
# ls1.append(10)
# print(ls1)
#
# ls1.append([15,20,25])
# print(ls1)
######################EXTEND()#########################

# ls=[]
# ls.extend((0,1,2,3,4,5,6,7,8,9))
# print(ls)
#
# ls.extend([11,22,33,44,55])
# print(ls)

# ls=[]
# ls.insert(0,1)
# print(ls)
#
# ls.insert(1,1)
# print(ls)
#
# ls.insert(9,2)
# print(ls)
#
# ls.insert(0,5)
# print(ls)
#
# ls.insert(2,6)
# print(ls)

# ls1=[1,2,3,4,5]
# ls2=ls1.copy()
# print(ls2)

# ls=[1,2,3,4,5,6]
# lsp=ls.pop(2)
# print(lsp)
# print(ls)

# ls=[1,2,3,4,5,6]
# lsp=ls.pop()
# print(lsp)
# print(ls)

# ls=[1,2,3,4,5,6]
# print(ls)
# ls.remove(4)
# print(ls)


# fname='babulu'
# lname='bhoi'
# print('fname+lname',fname+lname)

# a='10'
# b='20'
#
# print("a+b:",a+b)



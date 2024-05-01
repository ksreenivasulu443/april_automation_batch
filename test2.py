# ls = []
# print("type of ls ", type(ls))
# print("id(ls)", id(ls))
#
# ls2 = list()
#
# print("type of ls2 ", type(ls2))
#
# ls.append(1)
# print(ls)
#
# ls.append([1,2])
#
# print(ls)
#
# ls.extend([1,2,3])
# print(ls)
#
# print("id(ls)", id(ls))

import sys

# Create an empty list
my_list = []

# Print the size of the list object
print("Size of empty list:", sys.getsizeof(my_list))

# Append elements to the list
for i in range(10):
    my_list.append(i)

# Print the size of the list object after appending elements
print("Size of list with 10 elements:", sys.getsizeof(my_list))

# Print the length and capacity of the list
print("Length of list:", len(my_list))
print("Capacity of list:", my_list.__sizeof__())

import sys

# Create an empty tuple
my_tuple = ()

# Print the size of the tuple object
print("Size of empty tuple:", sys.getsizeof(my_tuple))

# Create a tuple with elements
my_tuple = (1, 2, 3, 4, 5,6,7,8,9,10)

# Print the size of the tuple object with elements
print("Size of tuple with elements:", sys.getsizeof(my_tuple))

a=10
print("Size of a with elements:", sys.getsizeof(a))

# Print the length of the tuple
print("Length of tuple:", len(my_tuple))

print("Capacity of my_tuple:", my_tuple.__sizeof__())

ls2 =[1,23,3]
ls3 = ls2

print("ls3", ls3)
print("ls2", ls2)

ls2.append(1)

print("ls3", ls3)
print("ls2", ls2)

ls4 = ls2.copy()
ls4.append(5)

print("ls3", ls2)
print("ls2", ls4)

#ls5 = ls2.shallo

print(ls2.index(3))

ls2.insert(10,8)

print("ls2", ls2)

ls2.pop()

print(ls2)
ls2.pop()
print(ls2)

ls2.remove(23)
print(ls2)

ls2.extend([1,2,3,4,4,8,19,20,212,212,45,2,3])

print(ls2)

ls2.reverse()

print(ls2)

ls2.reverse()

ls= [1,4,2,7,4,2,8]
ls.sort(reverse=True)

print(ls)

ls.reverse()

print(ls)





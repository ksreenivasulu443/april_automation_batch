"""This module file is create to practice python set datatypes
created by Sreeni on 05/03/2024 """

# Creating a set
s = {1, 6,5,2, 3, 4, 5,1,2,6}
d = {'name':'sreeni', 'college':'ABC'}
d2 = {}
s2 = set()

print("set is ", s)
print("d is ", d)
print("d2 is ", d2)
print("s2 is ", s2)
print("type of s is ", type(s))
print("type of d is ", type(d))
print("type of d2 is ", type(d2))
print("type of s2 is ", type(s2))

#print(s[0])
# s1 = list(s)
# print(s1[0])
print("methods available", dir(s))

# # Adding elements to a set
s.add(10)
s.add('Raghav')
print("my set after add", s)
s.update('sreeni') # list, str, tuple, set, dict, # we can't int, float, bool, complex


print("my set after update", s)

poped_element = s.pop()
print("my set after pop", s)
print("poped_element", poped_element)
s.pop()
print("my set after pop", s)
#
#Removing elements from a set
s.remove(4)
print("my set after remove", s)
s.discard(3)
print("my set after discard", s)
s.discard(3)
print("my set after discard", s)
# s.remove(4)
# print("my set after remove", s)
#
# Set operations
set1 = {1, 2, 3,2}
set2 = {3, 4, 5}
#
# Union
union_set = set1.union(set2)

print("union_set", union_set)
#
# #
# set1.update(s)
# print("unionall", set1)
#
# Intersection
intersection_set = set1.intersection(set2)
#
print("intersection_set",intersection_set)
#
# Difference
difference_set = set1.difference(set2)
#
print("difference_set",difference_set)
#
# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
#
print("symmetric_difference_set",symmetric_difference_set)
#
fs = frozenset(s)
print("type of fs", type(fs))
print("methods available in fs", dir(fs))
#
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = {5, 6, 7}
#
# # Using the update() method
# set1.update(set2)
#
# print(set1)
#
#
validation='count'
print("*" * 50)
print(f"{validation} has started")
print("*" * 50)

print("*" * 50)
print(f"{validation} has ended")
print("*" * 50)

str ='sreeni-kattu'

ls = str.split('-')
print(ls)

ls2 = list(str)
print(type(ls2))
print(ls2)


a = '10'
print("type of a",type(a))
b = '12-'
print("type of b",type(b))

a = int(a)
print("type of a after int convertion",type(a))
# b= int(b)

#a='10fhsafghasd'
print("type of a",type(a))
a=float(a)
print("type of a after float",a,type(a))

a= 10

a = str(a)

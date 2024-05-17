# # *************TUPLE****************
# A tuple in Python is similar to a list, but it's enclosed within parentheses ( ).
# Immutability: Tuples are immutable, meaning once created, their contents cannot be changed (you cannot add, remove, or modify elements).
# Order: Similar to lists, tuples also maintain the order of elements.
# Elements: Tuples can contain elements of different data types, just like lists.
# Indexing and Slicing: Similar to lists, elements in a tuple can be accessed using indices. Tuple slicing is also supported.
# e.g., first_tuple = (1, 2, 'hello', [3, 4], (5, 6), 1+2j,10.3)
# Location : (lat, lang)


# tuple1 = (10, 20, 30, 40, 50)
# print(tuple1)
#
# tuple2=tuple1[::-1]
# print(tuple2)

# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# print(tuple1[1][1])
#
# tuple=(50,)
# print(tuple)

# tuple1 = (10, 20, 30, 40)
# a=tuple1[0]
# b=tuple1[1]
# c=tuple1[2]
# d=tuple1[3]
# print("print(a)",a)
# print("print(b)",b)
# print("print(c)",c)
# print("print(d)",d)
#
# a,b,c,d=tuple1
# print("a,b,c,d:",a,b,c,d)
#
# --------Swap two tuples in Python------------

# tuple1 = (11, 22)
# tuple2 = (99, 88)
# print("before swapping:",tuple1,tuple2)
# tuple1,tuple2=tuple2,tuple1
# print("after swapping:",tuple1,tuple2)

tuple1 = (11,22,33,44,55,66)
tuple2 = tuple1[3:5]
print(tuple2)
tuple3=tuple1[0:4]
print(tuple3)
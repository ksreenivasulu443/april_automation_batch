"""This module file is create to practice python list datatypes
created by Sreeni on 05/01/2024 """
import sys
tuple1 = (1, 2.0, True, 1+2j, 'string')

print("tuple1 values", tuple1)
print("type of tuple1 is ", type(tuple1))
print("memory of tuple1", id(tuple1))

print("first element in tuple1 is ", tuple1[0], type(tuple1[0]),id(tuple1[0]) )
print("second element in tuple1 is ", tuple1[1],type(tuple1[1]),id(tuple1[1]))

print("tuple1[0:2]",tuple1[0:2] )

print("methods available in tuple", dir(tuple1))

print("tuple1.index(2.0)",tuple1.index(2.0))

ls = [1,2,3,4,5]
t =(1,2,3,4,5)



print("list size",sys.getsizeof(ls))


print("tuple size",sys.getsizeof(t))

# print("tuple")
# for i in t:
#     print(i, sys.getsizeof(i))

# for i in ls:
#     print(i, sys.getsizeof(i), sys.getrefcount(i))


# a= 1002+1j
# print(a, sys.getsizeof(a), sys.getrefcount(a)-1)

"""This module file is create to practice python list datatypes
created by Sreeni on 05/01/2024 """

tuple1 = (1, 2.0, True, 1+2j, 'string')

print("tuple1 values", tuple1)
print("type of tuple1 is ", type(tuple1))
print("memory of tuple1", id(tuple1))

print("first element in tuple1 is ", tuple1[0], type(tuple1[0]),id(tuple1[0]) )
print("second element in tuple1 is ", tuple1[1],type(tuple1[1]),id(tuple1[1]))

print("tuple1[0:2]",tuple1[0:2] )

print("methods available in tuple", dir(tuple1))

print("tuple1.index(2.0)",tuple1.index(2.0))



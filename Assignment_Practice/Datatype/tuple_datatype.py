tuple1 = (1, 2.0, True, 1 + 2j, 'string')
print("print the given tuple :", tuple1)

print("the values of tuple1 is : ", tuple1)
print("type of tuple1 is :", type(tuple1))
print("memory address of the tuple1 :", id(tuple1))

print("*" * 50)

print("the first_element in the tuple1 is :", tuple1[0])
print("the second_element in the tuple1 is :", tuple1[1])
print("the third_element in the tuple1 is :", tuple1[2])
print("the fourth_element in the tuple1 is :", tuple1[3])
print("the five_element in the tuple1 is :", tuple1[4])

print("*" * 50)

print("the first_element in the tuple1 is :", tuple1[0], type(tuple1[0]))
print("the second_element in the tuple1 is :", tuple1[1], type(tuple1[1]))
print("the third_element in the tuple1 is :", tuple1[2], type(tuple1[2]))
print("the fourth_element in the tuple1 is :", tuple1[3], type(tuple1[3]))
print("the five_element in the tuple1 is :", tuple1[4], type(tuple1[4]))

print("*" * 50)

print("the first_element in the tuple1 is :", tuple1[0], type(tuple1[0]), id(tuple1[0]))
print("the second_element in the tuple1 is :", tuple1[1], type(tuple1[1]), id(tuple1[1]))
print("the third_element in the tuple1 is :", tuple1[2], type(tuple1[2]), id(tuple1[2]))
print("the fourth_element in the tuple1 is :", tuple1[3], type(tuple1[3]), id(tuple1[3]))
print("the five_element in the tuple1 is :", tuple1[4], type(tuple1[4]), id(tuple1[4]))

print("*" * 50)

print("tuple1[0]:", tuple1[0])
print("tuple1[0::]:", tuple1[0::])
print("tuple1[0::]:", tuple1[0:3])

print("methods available in the tuple are :", dir(tuple))
"""'count', 'index'"""

print("-"*70)

tuple1 = (1, 2.0, True, 1 + 2j, 'string',2.0,'string',1,1)
print("print the index of the given tuple1.index(2.0):", tuple1.index(2.0))
print("print the count of the given tuple1.count(2.0):", tuple1.count(2.0))
print("print the count of the given tuple1.count(1):", tuple1.count(1))
print("print the count of the given tuple1.count(2):", tuple1.count(2))
print("print the count of the given tuple1.count(1+2j):", tuple1.count(1+2j))
print("print the count of the given tuple1.count('string'):", tuple1.count('string'))

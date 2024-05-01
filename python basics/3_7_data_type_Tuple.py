# Tuple(): is used to store the sequence of various types of data. this data type is Immutable

'''
* sequence of various types of data, means --- Heterogeneous objects are allowed
* Duplicates values are allowed
* insertion order required to preserve
* Immutable
* indexing applicable
* slicing applicable
* Values should be enclosed by Parenthesis ()
'''


x = (10, 20, "ajay", 50, "ram", 10)
print(x)

# Index & slice
print("-----Index & slice------")
print(x[1])
print(x[-5])
print(x[1:4])
print(x[::-1])

# count : count the repeated character in string
print("-----count of character in tuple------")
print(f"count of a character in {x} is :", x.count(10))
print(f"count of ram & a character in {x}", x.count('ram'), x.count('a'))

# len length of the string
print("-----length of string------")
print(f"length of {x} is ", len(x))

# sort
k = (1, 4, 2, 3, 5, 7, 6, 8, 9)
print("-----sort value in Tuple------")
print(sorted(k))
print(sorted(k, reverse=True))

# min & max value of tuple
print("-----in & max value of tuple------")
print(min(k))
print(max(k))

# packing and unpacking
print("-----packing and unpacking------")
a, b, c, d, e, f = x
print(f"unpacking tuple {x} and value of a is:", a)

lst = (a, b, c, d, e, f)
print("packing a, b, c, d, e, f as tuple:", lst)


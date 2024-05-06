# Set(): is used to store the sequence of various types of data where insertion order is not required to preserve
# and duplicates are not allowed they we should go for set data type

'''
* sequence of various types of data, means --- Heterogeneous objects are allowed
* insertion order is not required to preserve
* Duplicates values are not allowed
* Mutable --- add, remove, update, clear, copy the value
* indexing not applicable
* slicing not applicable
* Values should be enclosed by flower or curly bracket {}
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__',
'__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__',
'__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__',
'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__',
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update',
'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update',
'union', 'update']

'''

# Creating set
d = {9, 1, 3, 2, 6, 2, 3, 4, 7, 5, 8, 10}
print("Values of the set s is", d)
print("Type of s is ", type(d))

# identify the set
print("------identify the set-------")
e = set()
print("Type of e is ", type(e))

w = {}
print("Type of w is ", type(w))
# print(dir(set))

# Adding value into a set -- adding one values
print("------Adding single value into a set-------")
s = {10, 20, 30, 90, 20, 100}
s.add(50)
s.add("Ram")
print("check 50 and Ram added to the set s is ", s)

# Update the exists value into a set -- adding multiple values only text and int values
print("------Adding multiple value into a set-------")
s.update("Raju")
print("Set s after update is", s)

# Pop will delete the random element from the set
print("------Pop will remove the random element from the set-------")
s.pop()
print("Set s after pop is", s)

# Remove will delete the specific element from the set
print("------Remove will delete the specific element from the set-------")
s.remove("Ram")
print("Set s after remove is", s)

# Discard will delete the specific element is present in the set or else it will skip
print("------Discard will delete the specific element is present in the set or else it will skip -------")
s.discard(98)
print("Set s after discard is", s)
s.discard("R")
print("Set s after discard is", s)

# Set Operators
s1 = {1, 2, 3, 7, 4, 5, 6}
s2 = {3, 5, 8, 9, 2, 1, 2, 4}

union_all = s1.union(s2)
print("union_all set", union_all)

intersection_set = s1.intersection(s2)
print("intersection_set set1", intersection_set)


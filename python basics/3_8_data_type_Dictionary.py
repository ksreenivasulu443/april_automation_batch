
# Dictionary dict(): is used to store the sequence of various types of data in a group of values as key-value pair
# then we should go for dict data type

'''
* Dictionary it is key-value pair
* sequence of various types of data, means --- Heterogeneous objects are allowed
* insertion order is not required to preserve
* Key - Duplicates values are not allowed and immutable
* Mutable --- n[key]="value"
* indexing not applicable
* slicing not applicable
* Values should be enclosed by flower or curly bracket {}
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__',
  '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__',
  '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__',
  '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys',
  'get', 'items', 'keys', 'pop', '  popitem', 'setdefault', 'update', 'values']

variable[key]=value -- adding key & value in dictionary
'''

d = {1: "Arjun", 2: "Bharath", 3: "Chandu"}
print("Type of d is", type(d))
print("key and values in d is", d)

# append or add or insert key & value in dictionary
print("-------adding key & value in dictionary-------")
d[4] = "Raju"
print("Check 4 & raju added in d :", d)
d[5] = "Darshan"
d[6] = "Eshwar"
print("Check key and values are added in d :", d)

# Update value in dictionary and add new key and value
print("-------Update value in dictionary-------")
d.update({1: "Arun", 7: "Guru"})
print("Update value and added new key and value in d :", d)

ds = {102: 2, 103: 1, 104: 2}
print(ds)

# Get need to pass key
print("-------value of particular key by get method-------")
print("Display the value of particular key by get method", d.get(1))

# Pop
ds.pop(104)
print("value of the Pop", ds)

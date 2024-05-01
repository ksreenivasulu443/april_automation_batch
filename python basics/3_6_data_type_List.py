# List(): is used to store the sequence of various types of data. this data type is Mutable

# we want to represent a group of values as single entity where insertion order required to preserve and duplicates are
# allowed we should go for list data type

'''
* sequence of various types of data, means --- Heterogeneous objects are allowed
* insertion order required to preserve
* Duplicates values are allowed
* Mutable --- Append, insert, delete, update the value
* indexing applicable
* slicing applicable
* Values should be enclosed by square bracket []
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
'''

# assign multiple data type in list
ls = [5, 75.0, -10+2.5j, True, "Ram", (7, 5), [23, 78]]
print("list values :", ls)
print("type of the ls is", type(ls))
print("memory address of ls is", id(ls))

# Index list and data of index character
print("list 1st index and data type is :", ls[0], type(ls[0]), id(ls[0]))
print("list 1st index and data type is :", ls[1], type(ls[1]), id(ls[1]))
print("list 1st index and data type is :", ls[2], type(ls[2]), id(ls[2]))
print("list 1st index and data type is :", ls[3], type(ls[3]), id(ls[3]))
print("list 1st index and data type is :", ls[4], type(ls[4]), id(ls[4]))
print("list 1st index and data type is :", ls[5], type(ls[5]), id(ls[5]))
print("list 1st index and data type is :", ls[6], type(ls[6]), id(ls[6]))

print("methods available in list :", dir(list))
# methods available in list : ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# adding values in list methods [1 append, 2 insert, 3 extend]

# 1 append mean adding value at the end
ls2 = []
ls2.append(10)
ls2.append(20.05)
ls2.append(-10+2.5j)
ls2.append(False)
ls2.append("ram")
print(ls2)

#  2 insert mean adding value at specific index
ls2.insert(5, (2, 6, 9, 15, 57))
print(ls2)

# 3 extend mean adding value at the end
ls2.extend((1, 2, 3, 5, 10, 20.5, 10, 2))
ls2.extend("Mushroom")
print(ls2)

print("count os ls2 is ", ls2.count(5))

# Split function list can't split, string split convert list
print("-----Split function-----")
print("count os ls2 is".split())

# index
print("-----List index-----")
print(f'Forward 1st index character of {ls2} is', ls2[0])
print(f"in {ls2} 1st character is {ls2[0]}, 2st character is {ls2[1]}, and 3rd character is {ls[2]}")
print(f'Backward last index character of {ls2} is', ls2[-1])

# Slicing ex:
print("-------Slicing--------")
print(f'Forward Slicing characters of {ls2} is', ls2[0:5])
print(f'Backward Slicing characters of {ls2} is', ls2[-12:-1])
print(f"print 1 to 5th string from {ls2} is", ls2[2:5])

# skip character [start index no:end index no:skip no of character]
print(ls2[1:15:2])

# revers string by slicing
print(ls2[::-1])

# len length of the string
print("-----length of List------")
print(f"length of {ls2} is ", len(ls2))

# count : count the repeated character in string
print("-----count of character in List------")
print(f"count of a character in {ls2} is :", ls2.count("o"))
print(f"count of a & m character in {ls2}", ls2.count('a'), ls2.count('m'))

# replace
print("-----replace value of the List------")
n1 = ls2[2]=(10.1+2.5j)
print(f"change the lastname in fullname -10+2.5j to", n1)

# remove - the specific item, if similar item multiple then delete the 1st item
l = [1, 2, 3, 4, 1, 1, 2, 3, 'o', 4, 5, 6, 7, 'o']
print("-----Remove value in List------")
# a=l.remove(7)
# print(a)
l.remove(7)
print("",l)

# revers
print("-----Revers value in List------")
l.reverse()
print(l)

# sort
k=[1,4,2,3,5,7,6,8,9]
print("-----sort value in List------")
k.sort()
print(k)
k.sort(reverse=True)
print(k)


# 'pop, 'clear', 'copy'
print("-----pop, 'clear', 'copy'------")
k1 = k.copy()
print(k1)
print(k1.pop())
print(k1)
k1.clear()
print(k1)
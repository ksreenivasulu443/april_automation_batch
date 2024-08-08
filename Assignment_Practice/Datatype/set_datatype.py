# Creating a set

s = {1, 6, 5, 2, 3, 4, 5, 1, 2, 6}
d = {'name': 'sreeni', 'college': 'ABC'}

print("the value of the set is :", s)
print("the type of the set is :", type(s))
print("the address of the set is :", id(s))

print("the value of the dir is :", d)
print("the type of the dir is :", type(d))
print("the address of the dir is :", id(d))

d2 = {}
s2 = set()
print("type of d2 is ", type(d2))
print("type of s2 is ", type(s2))

print("set is ", s)
print("d is ", d)
print("d2 is ", d2)
print("s2 is ", s2)
print("type of s is ", type(s))
print("type of d is ", type(d))
print("type of d2 is ", type(d2))
print("type of s2 is ", type(s2))

s = {1, 6, 5, 2, 3, 4, 5, 1, 2, 6}
# print(s[0])
s1 = list(s)
print(s1[0])
# print("methods available", dir(s))
"""'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 
   'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
   'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'"""

# Adding elements to a set
s = {1, 6, 5, 2, 3, 4, 5, 1, 2, 6}
d = {'name': 'sreeni', 'college': 'ABC'}
s.add(10)
s.add('Raghav')
print("my set after add", s)

s.update({'11', '12', '13'})
s.update(('14', '15', '16'))
s.update(['17', '18', '19'])
print("print after update s:", s)

s.update('Nivi')
s.update('Pra@Ni', '999')
# s.update(10)  # list, str, tuple, set, dict, # we can't int, float, bool, complex
# s.update(10.5)
print("print after update s:", s)

s.update('sreeni')  # list, str, tuple, set, dict, # we can't int, float, bool, complex

print(s)
s.pop()
print("my set after pop", s)

print("-" * 150)
s1 = {1, 2, 3, 3, 4, 5, 'Nivi'}
print("my set before pop", s1)
s1.pop()
print("my set after pop", s1)
poped_element = s1.pop()
print("poped_element : ", poped_element)

print("-" * 50)

# Removing elements from a set

s1 = {1, 2, 3, 3, 4, 5, 'Nivi'}
print("my set before remove", s1)
s1.remove('Nivi')
print("my set after remove", s1)

# print("my set before remove", s1)
# s1.remove('200')
# print("my set after remove", s1)

s1.discard(3)
print("my set after discard", s1)

s1.discard(5)
print("my set after discard s1 :", s1)

s1.discard(5)
print("my set after discard s1 :", s1)

print("-" * 50)

# Set operations
set1 = {1, 2, 3, 2}
set2 = {3, 4, 5}

# Union
union_set = set1.union(set2)
print("union_set :", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("intersection_set :", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("difference_set", difference_set)

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("symmetric_difference_set :", symmetric_difference_set)

print("-" * 50)

fs = frozenset(s)
print("type of fs", type(fs))
# print("methods available in fs", dir(fs))
""" 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset',
    'issuperset','symmetric_difference', 'union'"""

print("-" * 50)

print(bool(0))
print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
# False True True True

print(type(range(5)))
# <class 'range'>

print(type({}))
# <class 'dict'>

str1 = 'Ault\'Kelly'
print(str1)

# str2 = 'Ault\\'Kelly'
# print(str2)

str3 = """Ault'Kelly"""
print(str3)

Name = 'Prashant\'Nivi'
print(Name)

print(type([]))
# <class 'list'>
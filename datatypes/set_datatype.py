"""This module file is create to practice python set datatypes
created by Sreeni on 05/02/2024 """

# Creating a set
s = {1, 6,5,2, 3, 4, 5}

print("set is ", s)

print("methods available", dir(s))

# Adding elements to a set
s.add(6)
s.pop()

print("my set after add", s)

# Removing elements from a set
s.remove(3)
print("my set after remove", s)
s.discard(3)
print("my set after remove", s)


# Set operations
set1 = {1, 2, 3,2}
set2 = {3, 4, 5}

# Union
union_set = set1.union(set2)

print("union_set", union_set)

#
set1.update(s)
print("unionall", set1)

# Intersection
intersection_set = set1.intersection(set2)

print("intersection_set",intersection_set)

# Difference
difference_set = set1.difference(set2)

print("difference_set",difference_set)

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)

print("symmetric_difference_set",symmetric_difference_set)

fs = frozenset(s)
print("type of fs", type(fs))
print("methods available in fs", dir(fs))

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

# Using the update() method
set1.update(set2)

print(set1)

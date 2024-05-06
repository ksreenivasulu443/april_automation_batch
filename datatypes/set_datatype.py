"""This module file is create to practice python set_datatype and
   created by Prashant on 03/05/2024"""

# creating a set
s = {1,2,3,5,6,4,8,8,0,1,2,9}
d = {'name':'prashant','college':'sdvs'}
d2 ={}
s2 = set()

print("set value s is :",s)
print("dir vue d is :",d)
print("set value s2 is :",s2)
print("dir value d2is :",d2)

print("type of set a is :",type(s))
print("type of dir d is :",type(d))
print("type of s2 is :",type(s2))
print("type of d2 is :",type(d2))

# print(s[0])
s1 = list(s)
print("index value of s1 is :",s1[1])

print("methods available in :",dir(s))
   # 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
   # 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
   # 'symmetric_difference','symmetric_difference_update', 'union', 'update']

# # Adding element to the set
s = {1,2,3,5,6,4,8,8,0,1,2,9}
print("my set values before adding :",s)
s.add(10)
print("my set values after adding :",s)
print("="*70)
s.add('prashant')

# # updating element to the set
s.update({11,12,13})
print("my set values after updating :",s)



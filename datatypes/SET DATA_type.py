"""This module file is create to practice python set datatypes
created by Lina on 05/04/2024 """
# creating set
s = {1, 2, 8, 9, 0, 5, 6, 9}
d = {'name': "Lina", 'School': "ABC"}
s1 = set()
d1 = {}
print("set is ", s)
print("d is ", d)
print("type of d is ", type(d))
print("type of s is", type(s))
print("s1 is ", s1)
print("d1 is ", d1)
print("type of s1 is ", type(s1))
print("Type of d1 is ", type(d1))

#print(s[0])--- here in set we not display the index position of element
#--if we need diplay the index position of the elemet then we need to set datatype convert to list

# ls = list(s)
 # print(ls)
# print(ls[1],ls[2])

# print("methods avilable in set ",dir(s))

s.add(10)
s.add(20)
s.add('Raghav')
s.add('Lina')
print("my set after add", s)
s.update('sreeni') # list, str, tuple, set, dict, # we can't int, float, bool, complex


print("my set after update", s)


# # Adding elements to a set
#s.add(10)
 #s.add("raghav")
 #print("my set after update ",s)
 #s.add('Raghav')
# print("my set after add", s)
# s.update('sreeni') # list, str, tuple, set, dict, # we can't int, float, bool, complex


# print("my set after update", s)
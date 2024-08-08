"""This module file is create to practice python dictionary datatype and created by Prashant"""

d = {}
print(d)
d1 = {1: 'Prashant', 2: 'Nivi', 3: 'Shruti'}
print(d1)

print("the value of the d is :", type(d))
print("the type of the d is :", type(d))
print("the address of the d is :", id(d))

print("methods available in the dir", dir(d))
"""'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
   'pop', 'popitem', 'setdefault', 'update', 'values'"""

# d[key] = value
d[1] = 'Prashant'
d[2] = 'Nivi'

print("d is :", d)
d.update({3: 'Shruti'})
print("d after update is :", d)
d.update({3: 'Shree'})
print("d after update is :", d)

d[8] = 1 + 2j
d[9] = 10.4
print("d value", d)

d3 = {1: 'sreeni', 2: 'hari', 1: 'Raghav', 1: 'ram'}

print("d3 is ", d3)

d4 = {1: 'sreeni', 2: 'sreeni', 3: 'raghav', 4: 'raghav'}
print("d4 is ", d4)

d = {1: 'sreeni', 2: "hari", 3: "ramesh"}
print(d)
print("d.get(1) :", d.get(1), len(d.get(1)))
print("d.get(2) :", d.get(2), len(d.get(2)))
print("len(d.get(1) :", len(d.get(1)))

print("length of dict", len(d))

print("keys available in dict", d.keys())
print("values available in dict", d.values())

d = {1: 'sreeni', 2: "hari", 3: "ramesh"}
# d.pop(3)
print("d values after pop ", d)
# d.popitem()
print("d values after popitem ", d)
print(d)

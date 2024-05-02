"""This module file is create to practice python dictionary datatypes
created by Sreeni on 05/02/2024 """


d = {1:'sreeni', 2:"hari", 3:"ramesh"}
# dictionary syntax d = {key:value, key2:value2, key3:value2...}
print("type of d ", type(d))
print("methods available in dict", dir(d))
print("d value before update", d)
# d[key] = value

d[4] = 'JK'

print("d after update ", d)

d.update({6:'KL', 1:('Virat', 'kohli')})

print("d after new insert and update key 1 data ", d)

d[8] = 1+2j
d[9] = 10.4
print("d value", d)
d3 = {1:'sreeni', 2:'hari', 1:'Raghav', 1:'ram'}

print("d3 is ", d3)

d4 = {1:'sreeni', 2:'sreeni', 3:'raghav', 4:'raghav'}
print("d4 is ", d4)

d = {1:'sreeni', 2:"hari", 3:"ramesh"}

print("d.get(1)",d.get(1), len(d.get(1)))
print("d.get(2)",d.get(2))

print("length of dict", len(d))

print("keys available in dict", d.keys())
print("values available in dict", d.values())

# d.pop(3)
print("d values after pop ", d)
d.popitem()
print("d values after popitem ", d)













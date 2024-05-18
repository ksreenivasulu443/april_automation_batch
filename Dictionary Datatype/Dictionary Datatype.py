
d={}

print("type of d", type(d))
print("methods available in d", dir(d))

d[1] = 'sandy'
d[2] = 'pushpa'

print("values in d", d)

d.update({3:'Hari'})
print("values in d", d)


d2 = {1:"Harish",2:"Appu",3:"Dhoni"}
print("Values in d2", d2)

d2[6] = 'Sid'
print("values in d2", d2)

d2.update({1:'MSD', 4:'KL'})
print("Values after update", d2)

print(d.get(1), len(d.get(1)))
print(d.get(2))
print(d.get(3))

print("length of dict", len(d))


print("Keys available in dict", d.keys())
print("Keys available in dict", d.values())

d.pop(3)
print("d values after pop",d)

d.popitem()
print("d values after popitem", d)




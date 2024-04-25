# 4. Bool(): data type to represent Boolean values, the values are "True" and "False"
# Ture = 1 , False = 0
'''
* hold the Boolean values
* indexing not applicable
* slicing not applicable
* Immutable (value assignments is not possible or not able to change the value)
'''

a = True

print('the vale of the count1 is', a)
print("type of the count1 is", type(a))
print("memory address of count1 is", id(a))

b = False

print('the vale of the count2 is', b)
print("type of the count2 is", type(b))
print("memory address of count2 is", id(b))


c = a+1+a+(b)
print('the vale of the c is', c)
print("type of the c is", type(c))
print("memory address of c is", id(c))

d = b+b
print('the vale of the c is', d)
print("type of the c is", type(d))
print("memory address of c is", id(d))


e = 20
f = 10
g = e < f
h = f < e
i = True + True
j = False + False


print(g)
print(h)
print(i)
print(j)
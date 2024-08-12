"""This module file is create to practice python Arithmetic_operators and created by Prashant"""

# PEMDAS rule

#
a = 10
print("print the value of a :", a)

a = b = c = 10  # z=10, b=10, c=10
print("print the value of a,b,c:", a, b, c)

x, y, z = 10, 20, 30
print("print the value of x,y,z:", x, y, z)

x, y, z = 10, 11, 13
print("print the value of x,y,z:", x, y, z)

x, y, z, b = 10, 20, 30, 40  # x=10, y=20, z=30, b=40
print("print the value of x,y,z,b:", x, y, z, b)
print("x :", x)
print("y :", y)
print("z :", z)
print("b :", b)

l, m = (1, 2, 3), [4, 5, 6]
print("l :", type(l))
print("m :", type(m))

# x=y=z=10
x, y, z = 10, 10, 10

print("x is type and id is ", x, type(x), id(x))
print("y is type and id os ", y, type(y), id(y))
print("z is type and id os ", z, type(z), id(z))

print("*" * 60)

# x=y=z=10
x, y, z = 10, 15, 20

print("x is type and id is ", x, type(x), id(x))
print("y is type and id os ", y, type(y), id(y))
print("z is type and id os ", z, type(z), id(z))

print("*" * 60)

d = 10
print("d value is :", d)
# d = d+2
# print("d value is after d=d+2 :",d)
d += 2
print("d value is after d=d+2 :", d)

print("*" * 60)

e = 5
print("e value is ", e)
# e = e-2
e -= 6  # e = e-6
print("e value after e-=2 :", e)

k = 5
print("the value of k is :", k)
# k = k*5
# print("the value of k after k=k*5 is:",k)
k *= 5
print("the value of k after k *=5 is :", k)

m = [1, 2]
print("the value list m is :", m)
m *= 3
print("the value list m after m =*3 is :", m)

m = 'Prashant'
print("the value str m is :", m)
m *= 3
print("the value str m after m =*3 is :", m)

# m *= 'Nivi' # TypeError: can't multiply sequence by non-int of type 'str'
# print("the value str m after m =*3 is :", m)


b = 'Prashant'
print("the value str b is :", b)
b += 'Nivi'
print("the value str b after m =*3 is :", b)

b = 'Prashant'
print("the value str b is :", b)
# b *= 'Nivi'
# print("the value str b after b *= 'Nivi' is :", b)

print("*" * 60)

h = 6
print("value of h is :", h)
h = h / 2
print("h value after h = h/2 :", h)
h /= 3
print("h value after h/=2 :", h)

print("*" * 60)

i = 2
print("the value of i is :", i)
# i = i**3
# print("the value of i after i = i**3 is :",i)
i **= 3
print("the value of i after i **=3 is :", i)

i = 3
print("i value is ", i)
i = i ** 3
# i **= 3 - 3  # 3 ** (3-3)
# i = i - 2
print("i value after i**3 ", i)

p = 4
n = 2
print("p value is :", p)
# p = p ** 4
# print("k value after p = p ** 4 is :", p)
p = p ** (4 - n)  # (4 - 2)
print("k value after p = p ** (4 - n) is :", p)

print("*" * 50)

x = 12
print("x value is : ", x)
# x = x % 2
# print("x value after x = x%2 is : ", x)
x %= 2
print("x value after x %= 2 is : ", x)

e = 13
print("e value is : ", e)
# e = e % 2
# print("e value after e = e%2 is : ", e)
e %= 2
print("e value after e %= 2 is : ", e)

print("*" * 50)

a = 9
b = 4
print("division of a, b", a / b)
print("floor of a, b", a // b)  # // - this is floor division

i = 9
j = 4
print("division of i, j :", i / j)
print("floor of i, j :", i // j)

y = 9.0
z = 4
print("division of, z :", y / z)
print("floor of y, z :", y // z)

y1 = 9.0
z1 = 4.5
print("division of y1, z1 :", y1 / z1)
print("floor of y1, z1 :", y1 // z1)
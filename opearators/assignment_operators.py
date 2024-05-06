"""this file is created to practice python assignment opearators
Created by Sreeni on 06/05/2024"""

a = 10
print("a value is ", a)

a = b = c = 15
a = 15
b = 15
c = 15
print("a,b,c values respect.. ", a, b, c)

x, y, z, c = 'sreeni', 10, 10, True

# print("x,y,z,c values resp", x,y,z,c)
print("x values is", x)
print("y values is", y)
print("z", z)
print("c", c)

l, m = (1, 2, 3), [4, 5, 6]

l = (1, 2, 3)
m = [4, 5, 6]

print("l", l, type(l))
print("m", m, type(m))

# x=y=z=10
x, y, z = 10, 10, 10

print("x is type and id is ", x, type(x), id(x))
print("y is type and id os ", y, type(y), id(y))
print("z is type and id os ", z, type(z), id(z))

d = 10
print("d value is ", d)
# d = d+2
d += 2
print("d value is after d+=2", d)

e = 5
print("e value is ", e)
# e = e-2
e -= 6  # e = e-6
print("e value after e-=2", e)

k = 'sreeni'
print("the value of k", k)
# k = k*4

k *= 7
print("the value of k after k*=4", k)

h = 6

print("value of h is", h)
# h = h/2
h /= 3

print("h value after h/=2", h)

i = 3
print("i value is ", i)
# i = i ** 3
i **= 3 - 3  # 3 ** (3-3)
i = i - 2
print("i value after i**3 ", i)

m = 12

print("m value is",m)
# m = m%2

m%=3
print("m value after m%2",m)

a= 9
b= 4

print("divison of a, b", a/b)
print("floor of a, b", a//b)

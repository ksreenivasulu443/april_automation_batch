# """This module file is create to practice python logical_operators and created by Prashant"""
#
# AND Condition
a = 10
b = 20
print("print the value a anb b is :", a and b)  # when both true, output will be right side value
print("print the value b anb a is :", b and a)

c = 40
d = 30
print("bool(c)", bool(c))
print("bool(d)", bool(d))
print("print the value a anb b is :", c and d)  # when both true, output will be right side value
print("print the value d anb c is :", d and c)

e = 0
f = 100
print("bool(e)", bool(e))
print("bool(f)", bool(f))
print("print the value e anb f is :", e and f)

g = 100
h = 0
print("bool(g)", bool(g))
print("bool(h)", bool(h))
print("print the value g anb h is :", g and h)

print("-" * 50)

# OR Condition

i = 40
j = 30
print("bool(i)", bool(i))
print("bool(j)", bool(j))
print("print the value i or b is :", i or j)  # when both true, output will be right side value
print("print the value j or i is :", j or i)

k = 0
l = 30
print("bool(k)", bool(k))
print("bool(l)", bool(l))
print("print the value k or l is :", k or l)  # when both true, output will be right side value
print("print the value l or k is :", l or k)

m = 10
n = 0
print("bool(m)", bool(m))
print("bool(n)", bool(n))
print("print the value m or l is :", m or n)  # when both true, output will be right side value
print("print the value n or m is :", n or m)

o = 0
p = 0
print("bool(o)", bool(o))
print("bool(p)", bool(p))
print("print the value o or p is :", o or n)  # when both true, output will be right side value
print("print the value p or o is :", p or o)

# Or output
# if both true then output will be left right
# if one value is true other value false then output will be True value
# if both false output is 0

print("-" * 50)

# NOT Condition

h1 = 25
print("h1 value and bool(h1)", h1, bool(h1))
print(" h1 not ", not h1)

h2 = 0
print("h2 value and bool(h2)", h1, bool(h2))
print(" h2 not ", not h2)

source = 10
target = 10
if source == target:
    print("source count and target is matching")
else:
    print("source count is and target not matching the deference is :", source - target)

source1 = 10
target1 = 11
if source1 == target1:
    print("source1 and target1 count is matching")
else:
    print("source1 count and target1 is not matching the deference is :", source1 - target1)

print("-" * 70)

a, b, c = 30, 20, 10

if a > b and a > c:  # False and True--> False
    print("a is maximum value")
elif b > a and b > c:
    print("b is maximum value")
else:
    print("c is maximum")

"""this file is created to practice python Logical_operators (class 14
) Created by khushboo on 07/05/2024"""

#logical operators

a= 100

b= 20

print("bool(a)", bool(a))
print("bool(b)", bool(b))

print(" a and b is", a and b) # when both true, ouput will be right side value

print(" a or b is", a or b) # when both true, ouput will be left side value

c= 0
d= 34
print("bool(c)", bool(c))
print("bool(d)", bool(d))
print(" c and d is", c and d) # when both true, ouput right side value


e = 0
f = 5

print("bool(e)", bool(e))
print("bool(f)", bool(f))
print(" e or f is", e or f)
#Or oupt
# if both true then output will be left right
# if one value is true other value false then output will be True value
# if both false output is 0

h = 0

print("h value and bool(h)", h, bool(h))
print(" h not ", not h)

a,b,c = 20,30,10

if a>b and a>c: # False and True--> False
    print("a is maximum value")
elif b>a and b>c:
    print("b is maximum value")
else:
    print("c is maximu")
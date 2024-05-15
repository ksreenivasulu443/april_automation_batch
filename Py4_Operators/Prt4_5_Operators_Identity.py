'''
Identity Operators:
identity operators for address or memory comparison.
2 identity operators are available
1. is
2. is not
r1 is r2 returns True if both r1 and r2 are pointing to the same object
r1 is not r2 returns True if both r1 and r2 are not pointing to the same object
'''

# immutable data type
a = 10
b = 5
c = 10
d = 2

tp1 = (1,2,3)
tp2 = (1,2,3)

# Methods "is"
print("------'Methods 'is' immutable data type'------")
print("memory location a is:", id(a), "memory location b is:", id(b))
print("memory location a is:", id(a), "memory location b is:", id(c))
print("identity a is b:", a is b) # If both address or memory location is not same, out put is Fail
print("identity a is b:", a is c) # If both address or memory location is not same, out put is Pass
print("identity tp1 is tp2:", tp1 is tp2) # If both address or memory location is not same, out put is Pass

# Mutable data type
ls1 = [1,2,3]
ls2 = [1,2,3]
print("------'Methods 'is' mutable data type'------")
print("memory location a is:", id(ls1), "memory location b is:", id(ls2))
print("identity ls1 is ls2:", ls1 is ls2) # If both address or memory location is not same, out put is Fail

# Methods "is not"
print("------'Methods 'is' mutable data type'------")
print("memory location a is:", id(ls1), "memory location b is:", id(ls2))
print("identity ls1 is ls2:", ls1 is not ls2) # If both address or memory location is same, out put is pass

# Methods "in"
print("------'Methods 'in' mutable data type'------")
print("membership d in ls1:", d in ls1) # If value present in variable, out put is Pass
print("membership tp1 in ls1:", tp1 in ls1)

# Methods "not in"
print("------'Methods 'in' mutable data type'------")
print("membership b in ls1:", b not in ls1) # If value present in variable, out put is Pass
print("membership tp1 in ls1:", tp1 not in ls1)
"""
Logical Operators:
and, or ,not
We can apply for all types.
For boolean types behaviour:
and ==>If both arguments are True then only result is True
or ====>If atleast one arugemnt is True then result is True
not ==>complement
1 or grater than one = true
0 = false
"""

# Methods "and"  If both arguments are True then only result is True
print("------'Methods 'and''------")
a = 10
b = 5
c = 0
d = 0
e = 1
print("Logical a==10 and b==5 is", a==10 and b==5)
print("Logical a==10 and b==5 is", a==15 and b==5)
print("Logical a and b is", a and b) # if both are ture, output is Right side Value
print("Logical a and b is", c and d) # if both are false, output is left side Value
print("Logical a and b is", d and e) # if one value is true, output is left side Value

# Methods "or"  If at least one argument is True then result is True
print("------'Methods 'or''------")
print("Logical a==10 or b==5 is", a==15 or b==5)
print("Logical a==10 or b==5 is", a==15 or b==7)
print("Logical a or b is", a or b) # if both are ture, output is Right side Value
print("Logical a or b is", c or d) # if both are false, output is left side Value
print("Logical a or b is", d or e) # if one value is true, output is Right side Value

# Methods "not"  complement
print("------'Methods 'not''------")
print("Logical not a==10 is", not a==5)
print("Logical not b==5 is", not b==5)
print("Logical not b is:", not b, "and boolean of b is:", bool(b)) # if bool ture, output is False
print("Logical not c is:", not c, "and boolean of c is:", bool(c)) # if bool False, output is True


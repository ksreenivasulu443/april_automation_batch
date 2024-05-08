'''

DataType: is represent the type of data present inside a variable.
In Python we are not required to specify the type explicitly.
based on value provided, the type will be assigned automatically, hence python is Dynamically typed language

Two Types of Data type:
1. Fundamental data type
2. Collection data type

1. Five Types of Fundamental data type:
   1) int()
   2) float()
   3) complex()
   4) bool()
   5) str()

2. Types of Collection data type:
   1) str
   2) bytes
   3) bytearray
   4) range
   5) list
   6) tuple
   7) set
   8) forzenset
   9) dict
'''


count = 10

print('the vale of the count1 is', count)
print("type of the count1 is", type(count))
print("memory address of count1 is", id(count))

count2 = 10

print('the vale of the count2 is', count2)
print("type of the count2 is", type(count2))
print("memory address of count2 is", id(count2))

count3 = 15

print('the vale of the count3 is', count3)
print("type of the count3 is", type(count3))
print("memory address of count3 is", id(count3))

count4 = -10

print('the vale of the count4 is', count4)
print("type of the count4 is", type(count4))
print("memory address of count4 is", id(count4))

# Ex:
a = 24
print(type(a))

# Types of whole number forms are (Decimal form, Binary form, Octal form, Hexadecimal form)
# *) Decimal: divided by 10 or base 10, allowed digits are: 0 to 9
b = 10

# *) Binary form: divided by 2 or base 2, allowed digits are: 0 & 1
c = 26
print("Binary form")
print(bin(c))
print(0b11010)

# *) Octal form: divided by 8 or base 8, allowed digits are: 0 & 7
d = 1650
print("Octal form")
print(oct(d))
print(0o3162)

# *) Hexadecimal form: divided by 16 or base 16, allowed digits are: 0 & 9, a-f
# a = 10, b=11, c=12, d=13, e=14, f=15
e = 5349
print("Hexadecimal form")
print(hex(e))
print(0x14e5)
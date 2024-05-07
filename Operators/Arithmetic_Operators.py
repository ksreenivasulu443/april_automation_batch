"""This module file is create to practice python Arithmetic_operators and
   created by Prashant on 07/05/2024"""

# PEMDAS rule

print("(8+2)*3/2 :",(8+2)*3/2)
print("(8+2)*3/2",(8+2)*3/2) # 10*3/2-->30/2--15.0
print("(8+2)/(2*3)", (8+2)/(2*3)) # 10/(2*3) --> 10/6 --1.66
print("(8+2)/2*3", (8+2)/2*3 ) # 10/2*3 --> 5.0*3--15.0
print("(8+2)/3**2+3*2",(8+2)/3**2+3*2) # 10/3**2+3*2 --> 10/9+3*2-->1.1+6--7.1

l = 2
m = 4
n = 6
o = 8
# print("(m-l)*n:",(m-l)*n)
# print(("the value of (l+m)*l/n =",(l+m)*l/n))
# print("(l*o)*m*6+(l+m)=",(l*o)*m*6+(l+m))
# print("the values of (l+m)*n/o)=",(l+m)*n/o)
# print("Value of (l + m) * n /0 = ",(l + m) * n /0)

o = ((l + m) * n) / o
print("Value of ((l + m) * n) / o is ",o)

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print("Value of (a + b) * c / d is ",  e)

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print("Value of ((a + b) * c) / d is ",  e)

e = (a + b) * (c / d)   # (30) * (15/5)
print("Value of (a + b) * (c / d) is ",  e)

e = a + (b * c) / d      #  20 + (150/5)
print("Value of a + (b * c) / d is ",  e)
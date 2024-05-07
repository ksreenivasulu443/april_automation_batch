"""
Assignment Operators: We can use assignment operator to assign value to the variable.

+= : x+=10 ====> x = x+10
 -= : x-=10 ====> x = x-10
 *= : x*=10 ====> x = x*10
 /= : x/=10 ====> x = x/10
 %= : x%=10 ====> x = x%10
 //= : x//=10 ====> x = x//10
 **= : x**=10 ====> x = x**10
&=
|=
^=
>>=
<<=

"""

a = 10
print("a value is :", a)

a, b, c = 15, 15, 15
print("a, b, c values is :", a, b, c)

x, y, z, c = 10.5, "Raju", 15, 12+67J
print("x, y, z, c values is :", x, y, z, c)

l, m = (1,2,4, "Raju"), [1, 3, 5, "Soma"]
print("l, m values is :", l, m)


# Methods += : x+=y ====> x = x+y
print("------'Methods += : x+=y ====> x = x+y'------")
xa = 10
xa+= 5
print("xa value after xa+= 5 is", xa)

# Methods -= : x-=y ====> x = x-y
print("------'Methods += : x-=y ====> x = x-y'------")
xb = 10
xa-= 7
print("xb value after xb-= 7 is", xb)

# Methods *= : x*=y ====> x = x*y
print("------'Methods *= : x*=y ====> x = x*y'------")
xc = 10
xc*= 2
print("xc value after xc*= 2 is", xc)

# Methods /= : x/=y ====> x = x/y
print("------'Methods /= : x/=y ====> x = x/y'------")
xd = 10
xd/= 3
print("xd value after xd/= 2 is", xd)

# Methods %= : x%=y ====> x = x%y -- remainder value
print("------'Methods %= : x%=y ====> x = x%y'------")
xe = 10
xe%= 1
print("xe value after xe%= 2 is", xe)

# Methods //= : x//=y ====> x = x//y -- without decimal
print("------'Methods /= : x/=y ====> x = x/y'------")
xf = 10
xf//= 3
print("xf value after xf//= 2 is", xf)

# Methods **= : x*=y ====> x = x**y exponential
print("------'Methods **= : x*=y ====> x = x**y'------")
xg = 10
xg**= 2-2
print("xg value after xg**= 2 is", xg)


# Operator Precedence or Pemdas rule:

# ()  Parenthesis
# **  exponential operator
# *,/,%,//  multiplication,division,modulo,floor division
# +,-  addition,subtraction


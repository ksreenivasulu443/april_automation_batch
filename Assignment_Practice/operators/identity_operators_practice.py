"""This module file is create to practice python identity_operators and created by Prashant"""

a = 10
b = 20
print("id(a) :", id(a))
print("id(b) :", id(b))
print("a is b :", a is b)

a1 = 10
b1 = 10
print("id(a1) :", id(a1))
print("id(b1) :", id(b1))
print("a1 is b1 :", a1 is b1)

ls1 = [1, 2, 3]
ls2 = [1, 2, 3]
print("id(ls1) :", id(ls1))
print("id(ls2) :", id(ls2))
print("ls is b1 :", ls1 is ls2)


# tuple
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print("the id(t1) is :", id(t1))
print("the id(t2) is :", id(t2))
print("the t1 is t2 is :", t1 is t2)

t3 = (1, 2, 3)
t4 = (1, 2, 3)
print("the id(t3) is :", id(t3))
print("the id(t4) is :", id(t4))
print("the t3 is not t4 is :", t3 is not t4) 

ls1 = [1, 2, 3]
ls2 = [1, 2, 3]
print("id(ls1) :", id(ls1))
print("id(ls2) :", id(ls2))
print("ls is not b1 :", ls1 is not ls2)

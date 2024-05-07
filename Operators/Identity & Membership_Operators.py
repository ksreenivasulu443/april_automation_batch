"""this file is created to practice python Identity & Membership_Operators (class 14
) Created by khushboo on 07/05/2024"""


a= 10

b= 10

print("id(a)", id(a))

print("id(b)", id(b))

print("a is b", a is b)

ls1 = [1,2,3]
ls2 = [1,2,3]

print("id(ls1)", id(ls1))

print("id(ls2)", id(ls2))

print("ls1 is ls2", ls1 is ls2)

t1 = (1,2,3)
t2 = (1,2,3)

print("id(t1)", id(t1))

print("id(t2)", id(t2))

print("t1 is not t2", t1 is not t2)

# ===========================================================

# Membership_Operators

ls1 = [1,2,3]

print("4 is present or not:", 4 in ls1 )

print("'r' is present or not:", 'R' not in 'sreeni')
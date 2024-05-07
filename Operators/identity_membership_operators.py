"""This module file is create to practice python identity_operators and
   created by Prashant on 07/05/2024"""

# identity_operators
# Is
# Is not

a = 10
b = 20

print("the id(a) is :",id(a))
print("the id(a) is :",id(b))

print("the a is b is :",a is b)

a = 10
b = 10
print("the id(a) is :",id(a))
print("the id(a) is :",id(b))

print("the a is b is :",a is b)

ls1 = [1,2,3]
ls2 = [1,2,3]
print("the id(ls1) is :",id(ls1))
print("the id(ls2) is :",id(ls2))

print("the ls1 is ls2 is :",ls1 is ls2)

t1 = (1,2,3)
t2 = (1,2,3)
print("the id(t1) is :",id(t1))
print("the id(t2) is :",id(t2))

print("the t1 is t2 is :",t1 is t2)

t1 = (1,2,3)
t2 = (1,2,3)
print("the id(t1) is :",id(t1))
print("the id(t2) is :",id(t2))

print("the t1 is not t2 is :",t1 is not t2)

"""This module file is create to practice python logical_operators and
   created by Prashant on 07/05/2024"""

# logical_operators
# And
# Or
# Not

# And condition
# print("And Condition")
# print("-"*15)
#
# a = 10
# b = 20
#
# print("the value of a and b is :",a and b)
# print("the value of b and a is :",b and a)
#
# # in And condition # when both true, output right side value
# # + * + = + true
# # + * - = - false
# # - * + = - false
# # - * - = - false
#
# print("bool(a):",bool(a))
# print("bool(b):",bool(b))
#
# c = 0
# d = 0
# print("the value of c and d is :",c and d)
# print("the value of d and c is :",d and c)
#
# print("bool(c) is :",bool(c))
# print("bool(d) is :",bool(d))
#
#
# # Or condition
# print("Or Condition")
# print("-"*13)
#
# # in And condition  # when both true, output left side value
# # + * + = + true
# # + * - = - true
# # - * + = - true
# # - * - = - false
#
# # + * + = + true
# # if both true then output will be left right
# a = 10
# b = 20
# print("the value of a or b is :",a or b)
# print("the value of b or a is :",b or a)
#
# a = -10
# b = 1
# print("the value of a or b is :",a or b)
# print("the value of b or a is :",b or a)
#
# # + * - = - true
# # if one value is true other value false then output will be True value
# a = 10
# b = 0
# print("the value of a or b is :",a or b)
# print("the value of b or a is :",b or a)
#
# # - * + = - true
# # if one value is true other value false then output will be True value
# a = 0
# b = 10
# print("the value of a or b is :",a or b)
# print("the value of b or a is :",b or a)
#
# # - * - = - false
# # if both false output is 0
# a = 0
# b = 0
# print("the value of a or b is :",a or b)
# print("the value of b or a is :",b or a)
#
#
# # Not condition
# print("Not Condition")
# print("-"*15)
#
# h = 25
# print("h value and bool(h):",bool(h))
# print("h not",not h)
#
# i = 0
# print("i value and bool(i):",bool(i))
# print("i not",not i)

a,b,c = 30,20,10
if a>b and a>c:
    print("print the a is max values")
elif b>a and b>c:
    print("print the b is max values")
else:
    print("then print c is max values")


a,b,c = 20,30,10
if a>b and a>c:
    print("print the a is max values")
elif b>a and b>c:
    print("print the b is max values")
else:
    print("then print c is max values")



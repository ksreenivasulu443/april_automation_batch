"""this module file is created to practice python functions
   and created by Prashant on 15/May/2024"""


# syntax:
# def function_name(parameter1,parameter2,parameter3,......,etc)
#     """doc string"""
#     #function body (set of instruction)
#     return results # (optional)

# def calc():
#     print("this is calculator function:", 3 + 4)
#
#
# def calc(a, b):
#     print("sum of two numbers:", a + b)
#
#
# calc(10, 20)
#
#
# def calc2(a, b, c):
#     # print("sum three numbers:", a + b + c)
#     print(f"sum three numbers {a},{b},{c}:", a + b + c)
#     print(f"sub three numbers {a},{b},{c}:", a - b - c)
#
# calc2(1, 2, 3)
# calc2(4, 5, 6)
# calc2(7, 8, 9)
# calc2(-1,-1,3)
# calc2(-1,-2,3)

# def calc3(c, d):
#     print(f"the values of {c} is:", c)
#     print(f"the values of {d} is:", d)
#     print("Multiplication of two numbers:", c * d)
#     print(f"Addition of two numbers {c},{d}:", c + d)
#     print(f"Sub of two numbers {c},{d}:", c - d)
#     print(f"division of two numbers {c},{d}:", c / d)
#
#
# calc3(1, 3)
#
# def calc3(c, d):
#     print(f"the values of {c} is:", c)
#     print(f"the values of {d} is:", d)
#     c = c - 1
#     print(f"the values of {c} after change list:", c)
#     print("Multiplication of two numbers:", c * d)
#     print(f"Addition of two numbers {c},{d}:", c + d)
#     print(f"Sub of two numbers {c},{d}:", c - d)
#     print(f"divi of two numbers {c},{d}:", c / d)


# calc3(5, 3)

# def calc4(a, b):
#     print("the values of a is :", a)
#     print("the values of b is :", b)
#     return a + b, a - b, a * b,a,b
#
# calc4(1, 2)
# result = calc4(1, 2)
# print("the result is;",result[0])
# print("the result is;",result[1])
# print("the result is;",result[2])
# print("the result is;",result[3])
# print("the result is;",result[4])

# def calc5(a, b):
#     print("a values:", a)
#     print("b values:", b)
#     return a + b, 100, 200
#
#
# calc5(2, 3)
# result = calc5(2, 3)
# print("the values of result:", result)
# print("the values of calc5(2,3):", calc5(2, 3))
# print("the index values of a+b is:", result[0])
# print("the index values of 100 is:", result[1])
# print("the index values of 200 is:", result[2])


def calc6(a, b):
    print("a value is ", a)
    print("b value is ", b)
    # print(f"sum of two numbers", a + b)
    # print(f"sub of two number", a - b)
    # print(f"mul of two number", a * b)
    # print(f"div of two number", a / b)
    return a + b, a - b, a * b, a / b, 1000, 'sreeni'

# calc6(10, 20)
result = calc6(10, 20)
print(result)
sub, sum, mul, div, sal, name = calc6(10, 20)

print("sum", sum)
print("sub", sub)
print("mul", mul)
print("div", div)
print("sal", sal)
print("name", name)



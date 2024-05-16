"""this module file is created to practice python functions
and created by sreeni on 15/May/2024"""


# syntax:
#
# def function_name(parameter1, parameter2, etc): --> parameters optional
#     """doc string"""
#     #function body( set of instrcutions)
#     return results ( optional )

def calc():
    """this is fucntion created to do calculation of two hard coded numbers, etc"""
    print("this is calculator function:", 3 + 4)


# calc()

def calc2(a, b, c):
    """this is fucntion created to do calculation of three numbers, etc"""
    print("a value is", a)
    print("b value is b", b)
    print("c value is b", c)
    print(f"Sum of three number {a}, {b}, {c}:", a + b + c)
    print(f"sub of three number {a}, {b}, {c}:", a - b - c)


# calc2(10,20,30)
# calc2(40,90,210)
# calc2(1,2,3)
# calc2(-1,-2,3)
# calc2(c=10,a=20,b=20)

def calc2(a, b):
    print("a value is", a)
    print("b value is ",b)
    #return 345


#print(calc2(1000, 250))

# result = calc2(10,20)
# print("result is ", result[2])

def calc2(a, b, c):
    print(f"Sum of three numbers {a},{b},{c}:",a+b+c)


def calc3(a,b):
    print("a value is ", a)
    print("b value is ",b )
    print(f"sum of two numbers", a+b)
    print(f"sub of two number", a-b)
    print(f"mul of two number", a*b)
    print(f"div of two number", a / b)
    return a+b, a-b, a*b, a/b,1000,'sreeni'

print(calc3(10,20))
sub, sum,mul, div, sal, name = calc3(10,20)

print("sum", sum)
print("sub", sub)
print("mul", mul)
print("div", div)
print("sal", sal)
print("name", name)

calc3(10)




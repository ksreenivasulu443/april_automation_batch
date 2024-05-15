'''Function:
If a group of statements is repeatedly required then it is not recommended to write these
statements everytime seperately.

Python supports 2 types of functions.
1. Built-in Functions
2. User Defined Functions


1. Built-in Functions:
The functions which are coming along with Python software automatically,are called built-in functions
or pre-defined functions
Eg:
id()
type()
input()
eval()
etc..

2. User Defined Functions:
The functions which are developed by programmer explicitly according to business
requirements ,are called user defined functions.

Syntax to create user defined functions:
def function_name(parameters) :
 """ doc string"""
'''


def calc():
    """ this is function created to do calculation of two numbers"""
    print("sum of 3 + 4 is", 3+4)


def calc2(a, b, c):
    """ this is function created to do calculation of three numbers"""
    print(f"sum of {a}, {b}, {c} is", a+b+c)
    print(f"subtraction of {a}, {b}, {c} is", -a - b + c)


def calc3(a, b, c):
    """ this is function created to do calculation of three numbers"""
    return a, b, c, a+b, -b+c, a+b+c, -a - b + c


def calc4(a, b, c):
    """ this is function created to do calculation of three numbers"""
    sum = a+b
    sub = b-c
    tsum = a+b+c
    tsub = -a - b + c
    return sum, sub, tsum, tsub


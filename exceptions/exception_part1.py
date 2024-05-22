"""This file created to practice exception """

print("First print")

print("hello world")
try:
    a = int(input("value of a :"))
    b = int(input("value of b :"))
    print("try block")
    sum = a + b
    sub = a-b
    mul = a*b
    div = a/b
    print(f"sum,sub,mul,div of {a} and {b} is resp ", sum,sub,mul, div)
    # ls =[0,1]
    # print(ls[2])
except ZeroDivisionError as e:
    print("error during calculation, please retry, error is ", e)
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / 1
    print(f"sum,sub,mul,div of {a} and {b} is resp ", sum, sub, mul, div)
except ValueError as e:
    print("error during calculation, please retry ", e)
except NameError as msg:
    c=25
    sum = a + b + c
    sub = a - b
    mul = a * b
    div = a / b
    print(f"sum,sub,mul,div of {a} and {b} is resp ", sum, sub, mul, div)
except:
    print("default exception" )







print("last print")


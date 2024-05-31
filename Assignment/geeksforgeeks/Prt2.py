# Given two numbers, write a Python code to find the Maximum of these two numbers


a = int(input("Enter number"))
b = int(input("Enter number"))



maximum = max(a, b)
print(maximum)

if a>b:
    print(f"In {a}, {b} Max value is", a)
else:
    if b>a:
        print(f"In {a}, {b} Max value is", b)


def max_vlu(a, b):
    if a > b:
        print(f"In {a}, {b} Max value is", a)
    else:
        if b > a:
            print(f"In function {a}, {b} Max value is", b)

max_vlu(a,b)



def max_vlue(d,e):
    sm = max(d, e)
    return sm
rs = max_vlue(2, 4)
rs1 = max_vlue(-1, -4)
print("positive number max value is", rs)
print("negative number max value is", rs1)



# lambda function

sm1 = lambda d, e: max(d, e)

print(sm1(-8, -11))
print(sm1(10.6, 10.5))

def calc(a, b, c,d=5):  # a,b,c parameters, d parameter default argument
    sum = a + b + c+d
    print("a value is", a)
    print("b value is", b)
    print("c value is", c)
    print("d value is", d)
    print("sum of a,b,c,d", sum)
    return sum


# calc(10, 12, 13)  # 10,20,30 positional arguments
# calc(12, 10, 20)  # 10,20,30 positional arguments
# # print("add_3_num", add_3_num)
#
# calc(a=10, b=12, c=13) # 10,20,30 keyword arguments
#
# calc(c=13, a=10, b=12) # 10,20,30 keyword arguments

# calc(10,20,30,12) d=5 will be overwritten with d=12

#calc(10,20,d=1,c=25) # 10,20 positional, c=25 is key word arg, d is default but overwritten with 1
# calc(a=10,b=20,1,25) # Alway positional argument should be passed as first and then keyword arguments
# calc(10,20,a=10,b=10)

# calc(a='sreeni',b='string',c='satya', d='huy')

# def student(name, m1,m2,m3,m4=0):
#     total_marks = m1+m2+m3
#     print(f"student name is {name} and marks are {m1,m2,m3} and sum marks is {m1+m2+m3}" )
#
#     print(name+":"+str(total_marks))
# student('sreeni', 10,35,46)
#
# student('sreeni',m1=10,m2=20, m3=50)

def calc2(a,b):
    return a+b
def calc3(a,b,c):
    return a+b+c


def calc4(a,b,c,d):
    return a+b+c+d

def calc5(a,b,c,d,e):
    return a+b+c+d+e

# print(calc2(10,20))
# print(calc3(10,20,30))

def calc(*args):
    print(args)
    print("type of args", type(args))
    sum = 0
    for i in args:
        sum = sum + i
    return sum

# num = input("enter value1:")
# numbers = num.split(',')
# print("numbers", numbers)
# print(calc(numbers))
# calc(10,20,30)
# calc(10,20,30,60)
# calc(1,2,3,4,4,6,7,8)

def calc(**kwargs):
    print(kwargs)
    print("kwargs", type(kwargs))
    sum=0
    for value in kwargs.values():
        sum= sum+value
    return sum

print(calc(a=10,b=20))


def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)

# f(3,2)
# f(10,20,30,40)

# f(25,50,arg4=100) #25,50,4,100
# f(arg4=2,arg1=3,arg2=4) # 3,4,4,2
# f()
# f(arg3=10,arg4=20,30,40)

# f(4,5,arg2=6) # error

# f(4,5,arg3=5,arg5=6)

def calc(*args):
    print(args)
    print("type of args", type(args))
    total = 0
    for i in args:
        total += i
    return total

num = input("Enter values separated by commas: ")
numbers = [int(x) for x in num.split(',')]  # Convert input values to integers
print("Numbers:", numbers)
print("Sum:", calc(*numbers))  # Unpack the list using * to pass individual numbers as arguments












# positional arguments
def calc(a,b,c,d=0):
    sum=a+b+c+d
    print('sum of a,b,c,d',sum)
    return sum
#calc(10,12,13) # 10,12,13 are positional arguments
#
# calc(a=10,b=12,c=13) # 10,12,13 are keyword arguments
# #note :order of the keywords can be any order
# calc(c=10,a=14,b=14) # 10,12,13 are keyword arguments

# calc(10,20,30)#for d default value get passed
# calc(10,20,30,40)#for d updated value get passed
# #calc(a=10,b=20,30,40)# always arguments starts with positional arguments then other arguments
# #calc(10,b=20,30,40)# in this case also fucntion throw error bcz after b=20 again we passed positional arguments
# calc(10,20,c=20,d=15)#combination of positional ,keyword argumenst

# def student_details(name,m1,m2,m3):
#     print(f'student name is  {name} and his marks{m1}+{m2}+{m3}',m1+m2+m3)
#     print(name+":"+str((m1 + m2 + m3)))
# student_details('sree',10,20,30)

#variable length arguments
# def calc3(*args):
#     print(args)
#     print('type of args',type(args))
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# print(calc3(10,20,30,30,10))

# variable length keyword arguments
# def calc4(**kwargu):
#     print(kwargu)
#     print('type of args',type(kwargu))
#     sum=0
#     for value in kwargu.values():
#         sum=sum+value
#     return sum
# print(calc4(a=10,b=20,c=30,d=30,e=10))

#code to pass variable length arguments using input method:
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
print("Sum:", calc(*numbers))



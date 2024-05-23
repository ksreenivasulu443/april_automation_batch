#
# def calc(a,b,c):
#     sum=a+b+c
#     print("a+b+c:",sum)
#     return sum
# calc(10,12,13)
# sumabc=calc(10,12,13)  #positional arguments
# print("sum of a,b,c:",sumabc)
# addabc=calc(a=10,b=12,c=13) #keyword arguments
# print("sum of a+b+c:",addabc)

# def student(name,m1,m2,m3):
#     sum=m1+m2+m3
#     print(f"student name is {name} and marks are{m1,m2,m3} and sum of marks is {sum}")
#     print(name+":"+str(sum))
#     return sum
# student('Babulu',10,20,30)
# res=student('Babulu',10,20,30)
# print("name,sum:",res)

# def calc2(a,b):
#     return a+b
# def calc3(a,b,c):
#     return a+b+c
# def calc4(a,b,c,d):
#     return a+b+c+d
# def calc5(a,b,c,d,e):
#     return a+b+c+d+e
#
# print("calc2:",calc2(10,20))
# print("calc3:",calc3(10,20,30))
# print("calc4:",calc4(10,20,30,40))
# print("calc5:",calc5(10,20,30,40,50))

#---variable length keyword arguments----
#----*args will take all the values as tuple------
# def calc(*args):
#     print("arguments:",args)
#     print("type of arguments:",type(args))
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# calc(10,20)
# res=calc(10,20)
# print("return sum:",res)
# calc(10,20,30)
# calc(10,20,30,40)

#---------keyword variable length arguments---------
# def calc(**kwargs):
#     print(kwargs)
#     print("type of kwargs:",type(kwargs))
#     sum=0
#     for value in kwargs.values():
#             sum=sum+value
#     return sum
#
# sum=(calc(a=10,b=20,c=30))
# print("sum1:",sum)

def calc(**kwargs):
    print(kwargs)
    print("type of kwargs:",type(kwargs))
    for key in kwargs.keys():
        return key

# key=(calc(a=10,b=20,c=30))


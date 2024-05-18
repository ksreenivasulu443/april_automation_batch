# positional arguments
# def calc(a,b,c,d=2):
#     sum=a+b+c+d
#     print('sum of a,b,c,d',sum)
#     # print("a:",a)
#     # print("b:", b)
#     # print("c:", c)
#     # print("d:", d)
#     return sum
#calc(10,12,13) # 10,12,13 are positional arguments
#
# print(calc(1,2,3))
# print("a,b,c,d:",10,12,13)
# print("sum:",calc(a=10,b=12,c=13)) # 10,12,13 are keyword arguments
# #note :order of the keywords can be any order
# a1=calc(c=10,a=14,b=14,d=7) # 10,12,13 are keyword arguments
# print(a1)

# calc(10,20,30)#for d default value get passed
# calc(10,20,30,40)#for d updated value get passed
# #calc(a=10,b=20,30,40)# always arguments starts with positional arguments then other arguments
# #calc(10,b=20,30,40)# in this case also fucntion throw error bcz after b=20 again we passed positional arguments
# calc(10,20,c=20,d=15)#combination of positional ,keyword argumenst

# def student_details(name,m1,m2,m3):
#     print(f'student name is  {name} and his marks{m1}+{m2}+{m3}',m1+m2+m3)
#     print(name+":"+str((m1 + m2 + m3)))
# student_details('sree',10,20,30)

# def calc(*args):
#     print(args)
#     print("type of args:",type(args))
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
#
# s1=calc(1,2)
# print(s1)
#
# def calc(**kwargs):
#     print(kwargs)
#     print("type of args:",type(kwargs))
#     sum=0
#
#     for i in kwargs.values():
#         sum=sum+i
#     return sum
#
# print(calc(a=1,b=2,c=3))

# variable length keyword arguments
# def calc4(**kwargu):
#     print(kwargu)
#     print('type of args',type(kwargu))
#     sum=0
#     for value in kwargu.values():
#         sum=sum+value
#     return sum
# print(calc4(a=10,b=20,c=30,d=30,e=10))


# def string_char_length(str1,char1)
#     str_cnt=string.count(char1)
#     return str_cnt


# def max_no(a,b,c):
#     number_max=max(a,b,c)
#     return number_max
# print("max of 3 numbers:",max_no(1,2,30))

def fact_num(fact):
    fact=1
    for i in range(1,i+1):
        fact=fact*i
    return fact
print(f"factorials of {fact} is:",fact)


#
# def factorial(n):
#     result=1
#     for i in range(1,n+1):
#         result*=i
#         print("factorial ")




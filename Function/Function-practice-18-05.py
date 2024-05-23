"""def function_name(parameter1,parameter2)
function body
statements to perform tasks
return results"""


# def calc3(a,b,c):
#     print(f"sum of there numbers{a},{b},{c}:",a+b+c)

# calc3(1,2,3)
# calc3(-1,10,30)
# calc3(100,900,0)
# def calc2(a,b):
#     print("a value is:",a)
#     print("b value is:",b)
#     #return a+b,a-b,a,b
#     return a*b
# #print(calc2(20,10))
# # result=calc2(10,20)
# # print("result is ",result)
# result=calc2(10,20)
# #print("print result is:",result[0],result[1],result[2],result[3])
# print("print results is",result)

# def calc3(a,b):
#     print("a value is ",a)
#     print("b value is ",b)
#     return a+b,a-b,a/b,a*b,9000,'basha'
# add,sub,div,mul,sal,name=calc3(10,20)
# print("add",add)
# print("sub",sub)
# print("div",div)
# print("mul",mul)
# print("sal ",sal)
# print("name",name)

#
# def calc4(a,b,c,d=6):
#     sum=a+b+c+d
#     print("sum of a,b,c,d is",sum)
#     print("a values is ",a)
#     print("b values is ",b)
#     print("c values is ",c)
#     print("d values is ",d)
#     return sum
# # add_3_num=calc4(10,11,12)
# # print("add_3_num",add_3_num)
# # calc4(1,2,3,10)  #positional arguments
# calc4(10,20,c=30,d=100)

# def student(name,m1,m2,m3):
#     total_marks=m1+m2+m3
#     print(f"student name {name} and sum of marks are {total_marks}")
#     #print(name+":"+str(total_marks))
# student("Mehaboob Basha",30,40,20)

### args
# def calc(*args):
#      #print(args)
#     sum = 0
#     for i in args:
#         sum = sum +i
#     return sum
#
# print(calc(10,20,30))

# def calc(**kwargs):
#     print(kwargs)
#     Sum = 0
#     for value in kwargs.values():
#         Sum = Sum + value
#     return Sum
#
#
# print(calc(x=100, y=140, a=10, b=20, c=30))
#
# string='Mehaboob'
# string_char='M'
def findstr(str1,char1):
    str_cnt=str1.count(char1)
    return str1,char1,str_cnt
str2=input("enter your string:").lower()
char2=input("provide your char to count:").lower()
result=findstr(str2,char2)
print(result)

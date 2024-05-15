"""this module file is created to practice function by Sreenivas on 15th may 2024"""

# syntax:
# def function_name(parameter1,parameter2...):
#      '''doc strings'''
#      function body(set of instructions)
#      return result(optional)

# def Calc():
#     print('this is the calculator fucntion',3+4)
# def Calc2(a,b,c):
#     print(f'sum of 3 numbers {a},{b},{c}',a+b+c)
#     print(f'sum of 3 numbers {a},{b},{c}', a - b - c)
# Calc2(10,20,30)
# Calc2(1,2,3)
# Calc2(a=10,b=20,c=30)
# Calc2(c=10,a=20,b=30)
# return function
# def Calc3(a,b):
#     print('a is ',a)
#     print('b is ', b)
#     #print(f'sum of 2 numbers {a},{b},{c}', a + b + c)
#     print(f'sum of 2 numbers {a},{b}', a + b )
# Calc3
# def Calc4(a,b):
#     print('a is ',a)
#     print('b is ', b)
#     #print(f'sum of 2 numbers {a},{b},{c}', a + b + c)
#     print(f'sum of 2 numbers {a},{b}', a + b )
#     return a+b
# print(Calc4(10,20))
# result=Calc4(20,30)
# print(result)

def Calc5(a,b):
    print('a is ',a)
    print('b is ', b)
    #print(f'sum of 2 numbers {a},{b},{c}', a + b + c)
    # print(f'sum of 2 numbers {a},{b}', a + b )
    # print(f'sub of 2 numbers {a},{b}', a - b)
    # print(f'multi of 2 numbers {a},{b}', a * b)
    # print(f'division of 2 numbers {a},{b}', a / b)
    return a+b,a-b,a*b,a/b,1000,'sree'

#result=Calc5(10,20)
sum,sub,mul,div,sal,name=Calc5(10,20)
#print(result)
print(sum)
print(sub)
print(mul)
print(div)
print(sal)
print(name)

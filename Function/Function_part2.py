# from Function.Funciton_part1 import calc
# calc()

# def calc(a,b,c):
#     sum=a+b+c
#     print("sub of a,b,c are",sum)
#     return sum
# calc(10,12,13)   #10,12,13 are keyword arguments

# def calc2(*args):
#     print(args)
# # calc2(10,20)
# # calc2(10,20,30)
# # calc2(1,2,3,4,5)
#     sum=0
#     for i in args:
#          sum=sum+i
#     return sum
# print(calc2(1,2,3,4,5))

#max of 3 numbers

#
# def max_num(a,b,c):
#     number_max=max(a,b,c)
#     return number_max
# print(max_num(1,5,99))


# #factorial number
# def fact_num(a):
#     result=1
#     for i in range(1,a+1):
#         result=result+1
#         print(result)
# fact_num(9)
#
# #OR

def fact(n):
    if n ==0:
        return 1
    else:
        return n * fact(n-1)
print(fact(3))






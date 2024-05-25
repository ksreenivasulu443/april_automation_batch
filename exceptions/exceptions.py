# try:
#     a=int(input('enter a num:'))
#     b=int(input('enter a num:'))
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     print('sum,sub,mul,div',sum,sub,mul,div)
#     print('last print')
# except:
#     print('error during calculation,please retry')

##################################################################

try:
    a=int(input('enter a num:'))
    b=int(input('enter a num:'))
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    nsqrt=a**0.5
    print('sum,sub,mul,div',sum,sub,mul,div)
    print('last print')
except ZeroDivisionError as e:
    print('ZeroDivisionError when denominator is 0')
except ValueError as e:
    print('ValueError when invalid value')




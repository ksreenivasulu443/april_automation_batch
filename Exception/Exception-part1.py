#this file is created for file exception

print("hello world")
try:
    a=int(input("value of a:"))
    b=int(input("value of a:"))
    print("print try block")
    sum=a+b
    sub=a-b
    div=a/b
    print(f"sum and sub are ",sum,sub,div)
except ZeroDivisionError as e:
    print("error during calculation, please retry,error is",e)
except ValueError as d:
    print("error during calculation, please retry,error is",d)
print("last print")
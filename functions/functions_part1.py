

def calc():
    print("this is calc function:",3+7)
calc()

def calc2(a,b,c):
    print(f"sum of 3 numbers {a},{b},{c} :",a+b+c)
    print(f"sub of 3 numbers {a},{b},{c} :",a-b-c)
calc2(10,20,30)
calc2(-1,-2,-3)

def calc3(a,b):
    print("a:",a)
    print("b:",b)
    print("addition:",a+b)
    print("substraction",a-b)
    print("multiplication:",a*b)
    print("division:",a/b)
    return(a+b,a-b,a*b,a/b)

print(calc3(10,20))
sum,sub,mul,div=calc3(10,20)
print("sum:",sum)
print("sub:",sub)
print("mul:",mul)
print("div:",div)
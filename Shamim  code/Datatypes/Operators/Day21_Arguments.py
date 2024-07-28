def calc(a,b,c):#this is positional argument
   sum = a+b+c
   print("value of a is", a)
   print("value of b is", b)
   print("sum of a,b,c is", sum)
   return sum# if we want to get return value then use below print
print(calc(10,20,30))#this is positional argument
#calc(a:40,b:30,c;70)
####################################################
def calc1(a,b,c):#this is keyword argument
   sum = a+b+c
   print("value of a is", a)
   print("value of b is", b)
   print("sum of a,b,c is", sum)
   return sum# if we want to get return value then use below print
print(calc1(a=80,b=50,c=70))#this is keyword argument

############################################

def calc2(a,b,c,d=0):#here d is default argument
   sum = a+b+c
   print("value of a is", a)
   print("value of b is", b)
   print("value of c is", c)
   print("value of d is", d)
   print("sum of a,b,c ,d is", sum)
   return sum# if we want to get return value then use below print
print(calc2(a=80,b=50,c=70,d=10))#this is default argument

#############################################

#Variable length argumen:
def calc3(*shamim):
    sum = 0
    for i in shamim:
        sum = sum + i
    return sum
print(calc3(10,60,50,30,30,20,40,100))# in variable length we can provide number of arguments
###############################################
#Variable length keyword arguments
def calc4(**shamim):
    sum = 0
    for value in shamim.values():
        sum = sum + value
    return sum
print(calc4(a=10,b=60,c=50,d=30,e=30,f=22))
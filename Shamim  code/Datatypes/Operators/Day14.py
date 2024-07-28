#PEMDAS rules(p
print((8+2)*3/2)#10*3/2 --->30/2---15
print((8+2)/(2*3))
print((8+2)/3**2+3*2)#10/3**2+3*2---10/9+3*2-----1.1+6----7.111

 #comparison operator:it will give always true or false values

a = 10   #(= is assignment operator, == is comparison operator)
b = 10
print("a==b",a==b)
print("a!=b",a!=b)

x = 10
y = 25
print("x==y",x==y)
print("x!=y",x!=y)
print("x>y",x>y)
print("x<y",x<y)
print("x>=y",x>=y)
print("x<=y",x<=y)

source_count=10
target_count=10

if source_count == target_count:
    print("count is matching and test case is pass")
else:
    print("count is not matching and difference is",source_count-target_count)



        #Logical operators:AND ,OR, NOT
#AND
c= 90
d= 30
x= 0
print("bool(c)",bool(c))
print("bool(d)",bool(d))
print("bool(x)",bool(x))
print("c and d is",c and d)# it (and)will take right side value
#OR
e = 4
f = 0
print("bool(e)",bool(e))
print("bool(f)",bool(f))
print("e or f is",e or f)# it(or) will take left side value
#not (it will convert true to false ,false to true)
h = 25
print("h value",bool(h))
print("h not",not h)

a,b,c = 30,20,10

if a>b and a>c:   #TRUE TRUE then true so it will print a max
    print(" a max value")
elif b>a and b>c:
    print(" b is max value")
else:
    print("c is max)")

#Logical operators

# a=10
#
# b=20
#
# print("a and b is ",a and b )

c = 1
d = 0

print("bool(c)",bool(c))
print("bool(d)",bool(d))
print("c and d",c and d)

e=1
f=5

print("bool(e)",bool(e))
print("bool(e)",bool(f))
print("e or f",e or f)

a,b,c=30,20,10

if a>b and a>c:
    print("a is max value")
elif b>a and b>c:
    print("b is max value")
else:
    print("c is max")


ls1=[1,2,3]
ls2=[1,2,3]

print("id(ls1)",id(ls1))
print("id(ls2)",id(ls2))

print("id(ls1) and id(ls2)",ls1 is ls2)
# o/p
# id(ls1) 1721132727296
# id(ls2) 1721133014528
# id(ls1) and id(ls2) False

tuple1=(1,2,3)
tuple2=(1,2,3)

print("id(tuple1)",id(tuple1))
print("id(tuple2)",id(tuple2))

print("id(tuple1) and id(tuple2)",tuple1 is tuple2)
# output id(tuple1) 1721133055104
# id(tuple2) 1721133055104
# id(tuple1) and id(tuple2) True


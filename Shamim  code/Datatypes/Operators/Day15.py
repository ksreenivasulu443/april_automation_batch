a = 10
b = 10
print("id(a)",id(a))
print("id(b)",id(b))
print("a is b",a is b)# "is" is provide the if both memory locatopn is same then it will true

#List:mutualble in nature(value will add and remove) so memory loction is different
ls1 =[1,2,3]
ls2 =[1,2,3]
print("id(ls1)",id(ls1))
print("id(ls2)",id(ls2))
print("ls1 is ls1",ls1 is ls1) #list will be mutualble in nature(value will add and remove) so memory location
# will different but output will true

#Tuple:Immutalble in nature(value will not add and remove)  so memory loction is same output will true

t1 =(1,2,3)
t2 =(1,2,3)
print("id(t1)",id(t1))
print("id(t2)",id(t2))
print("t1 is t1",t1 is t1) #list will be mutualble in nature(value will add and remove) so memory location
# will different but output will true

#is not operator: #list will be mutualble in nature(value will add and remove) so memory location
# will different but output will false.
t1 =(1,2,3)
t2 =(1,2,3)
print("id(t1)",id(t1))
print("id(t2)",id(t2))
print("t1 is not t1",t1 is not t1)

#Membership operator: "in" and "not in"

ls1 = [1,2,3]
print("1 is present or not",1 in ls1)
print("1 is present or not",1 not in ls1)

#############################################################3
# if,if elif ,else logic

name = 'shamim'
if name == 'rehan':
    print(f"hellow{name},goodmorning")
elif name == 'xy':
    print(f"hellow {name},goodmorning")
else:
    print("condition not satisfy")

name1 = 'shamim'
if name1 == 'rehan':
    print(f"hellow{name1},goodmorning")
elif name1 == 'shamim':
    print(f"hellow {name1},goodmorning")
else:
    print("condition not satisfy")

name2 = 'shamim'
if name2 == 'shamim':
    print(f"hellow shamim",goodmorning)
elif   name2 == 'rehan':
     print(f"hellow rehan")
else:
    print("condition not satisfy")
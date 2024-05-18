

ls = [1,2.0,True,1+2j,'string']

print("list values", ls)
print("type of ls is",type(ls))
print("memory of lis", id(ls))

print("first element in ls is", ls[0], type(ls[0]), id(ls[0]))

ls2=[]
print("list 2 values is", ls2)
print("list 2 values is", type[ls2])
print("list 2 values is", id(ls2))

print("after append")
ls2.append(5)
print("list values in ", ls2)
print("type of ls2 is", type(ls2))
print("memory of ls2 is", id(ls2))

ls2.insert(0,11)
print("list values in ", ls2)
print("type of ls2 is", type(ls2))
print("memory of ls2 is", id(ls2))

ls2.extend((22,33,44,1,1,1,1))
print("list values is", ls2)

print("count of 1 in the list is", ls2.count(1))

ls3 = ls2.copy()
print("ls3", ls3)

ls2.pop()
print("after pop")
print("ls2", ls2)
print("ls3",ls3)

ls6=[1,2,3]
ls7=[8,9,10]

print("addition of list", ls6+ls7)
print("multiplication of list is", ls6*2)



















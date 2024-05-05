import sys

ls =[1,2,3,4,5,6]

p =(1,2,3,4,5,6)

print ("print list values", sys.getsizeof(ls))

print ("print Tuple values", sys.getsizeof(p))

#print("list of python files:",dir(ls))
# ['append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# ls.append(50)
#
# print(ls)

ls3 = ls.copy()
print(ls3)
print(ls)

#ls3.pop(1)
ls3.remove(1)
print("After pop",ls3)

ls2=ls
print("This is ls2 values",ls2)
print("This is ls values",ls)

ls2.pop()

print("This is ls2 values",ls2)
print("This is ls values",ls)

#count()

B = [1,2,3,4,5,6,7,3,3,3,3]
#extend
B.extend(ls2)
print(B)

#'insert', 'pop', 'remove', 'reverse', 'sort'
#'insert'
print(f"position of index value 5 in {B} list: ",B.index(5))

#Reverse

#print(f"list of {B} values",B.reverse())
B.reverse()
print(f"list of {B} values")

B.sort()
print("sorting The {B} balue: ",B)

B.reverse()
print(B)

x=B[8:-2:1]

x.reverse()

print(x)



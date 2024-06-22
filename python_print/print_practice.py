""" This file is created to practice python print function
    created by: Sreeni on 04/19/2024
"""
#Import section
import sys
import time

#Variable creation
a = 10
b = '10'
c = 'sreeni'
d = 10.5

#Priniting type of variables using print function and type function
print("type of a ", type(a))
print("type of b ", type(b))
print("type of c ", type(c))
print("type of d ", type(d))

print("type of [10,'10', 'sreeni',10.5] ", type([10,'10', 'sreeni',10.5]))

e = 10


print("memory of a ",id(a))
print("memory of e ",id(e))

f = 10
print("memory of f ",id(f),id(e), end='\n',sep='-')
print("memory of d ",id(d))
print("memory of b ",id(b))


# writing output to file
file = open('test.txt', 'a')
# original = sys.stdout
sys.stdout = file

print(a,b, sep=' ', end='\n', file=file, flush=True)
print(a,b, flush=False)
print(a,b, flush=False)
print(a,b,c ,flush=False)

for i in range(1,10000):
    print(i,sep=' ', end='\n', file=file, flush=True)

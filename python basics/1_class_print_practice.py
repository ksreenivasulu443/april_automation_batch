import sys

'''
Some of the basic function :-
----------------------------
Python support many function, some of those are-- "print()", "type()", "id()"
print(): this function displays the output on the screen
type(): this function checks the data type of specific variable
id(): this function find the address of variable
help(): supporting more low level info, supporting function & with examples
dir(): this function helps to get the available methods
examples mention below
'''

print("Hello World!")

print("Hello World!", "Welcome to ETL Automation")

a = 10
b = 2
print(a)
print("Value of a is:", a)
print(a, b, sep=",")
c = 20
d = 50
e = 100
print("Hello World!", "Welcome to ETL Automation", sep=",")

print(a, b, c, d, e, sep=",")

print("sum of a,b,c,d,e", a+b+c+d+e)
print("*"*50)
name = "Ajay"
Age = 29

print(F"name is {name} and age is {Age}")
print("name is", name, "and Age is", Age)

source_cnt = 20
target_cnt = 40

print(F"name is {source_cnt} and age is {target_cnt}")
print("name is", source_cnt, "and Age is", target_cnt, sep='')

file = open(r"/text.txt", 'a')
original = sys.stdout
sys.stdout = file

print(source_cnt, target_cnt, sep='-', end='\t', file=file)
print("Execution is completed!!!")
print("hello world")

print("hello world")

for i in range(1, 10):
    print(i)

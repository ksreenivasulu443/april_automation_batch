"""this file is created to practice python for_loop (class 17
) Created by khushboo on 10/05/2024"""

"""this file is created to practice for loop"""

ls = [1,2,3,4]#==> [1,4,9,16]

#syntax for loop

# for element in collection datat type/ string type:
#     code
for item in ls:
    print("element is", item)

#########################################################
t = (4,5,6)

for element in t:
    print("the value available is", element)
    print("this code is inside of for loop")
    print("hello this for loop")

print("out side of for loop")
#########################################################
str  = '!s,r,e,476327854@e,n,i'
for i in str:
    print("character in str",i )
#########################################################
dict = {101:'sreeni', 102:'Rahul', 103:'Raghav'}

print("dict.item()", dict.items())

print("dict", dict)
print("dict keys", dict.keys())
print("dict values", dict.values())

for key in dict.keys():
    print("key is", key)

for value in dict.values():
    print("value is",value)

for i, j in dict.items():
    print(f"key is {i} and value is {j}")

# ls = [1, 2, 3]  # ==> [1,4,9,16]
#
print("list beore square", ls)
ls[0] = ls[0] * ls[0]
ls[1] = ls[1] * ls[1]
ls[2] = ls[2] * ls[2]

print("list after square", ls)

ls2 = [4, 5, 6, 7, 8, 9, 10]
print("list before square", ls2)
ls3 = []
for i in ls2:
    print(f"{i}*{i}", i * i)
    ls3.append(i * i)

print("list before square", ls3)

ls3 = [1, 2, 3, 4, 5, 6, 8]
# print if number is even number

ls_odd =[]
ls_even=[]
for i in ls3:
    if i % 2 == 0:# 1%2 ==0
        print(f"{i} is even number")
        ls_even.append(i)
    else:
        print(f"{i} is odd number")
        ls_odd.append(i)


print("ls_odd", ls_odd)
print("ls_even", ls_even)

age = (10,24,17,35,90,76)

eligible_count = 0
non_eligible_count =0

for i in age:
    if i >=18:
        print(f"{i} is eligible for vote")
        eligible_count = eligible_count + 1
    else:
        print(f"{i} not eligible for vote")
        #non_eligible_count = non_eligible_count+1
        non_eligible_count += 1


print("eligible_count" , eligible_count)
print("non_eligible_count" , non_eligible_count)

r = range(1,10,2)

print("type of r", type(r))
print("r value is", r)
import random

for i in range(120,100,-5):
    print(i)
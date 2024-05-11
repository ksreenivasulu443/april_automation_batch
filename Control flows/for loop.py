# """this file is created to practice python for loop controls """"""
# Created by Lina on 010/05/2024"""
"""this file is created to practice for loop"""
# ls = [1, 2, 3, 4]  # ==>[1, 4, 9, 16]
#
# # syntax for loop
# # for element in collection datat type/ string type:
# # #     code
#
# for item in ls:
#     print("element is", item)
#     print(" square of element is", item * item)
##########################################################

# t = (4, 5, 6)
# for element in t:
#     print("the value available is", element)
#     print("this code is inside of for loop")
#     print("hellow this for loop")
#
# ls2 = [4, 5, 6, 7, 8, 9, 10]
# print("list before square", ls2)
# ls3 = []
# for i in ls2:
#     print(f"(i)*(i)", i * i)
#     ls3.append(i * i)
# print("list before square", ls3)

# str1 = 'lina@#$%3456jmhndr%'
# for i in str:
#     print("character in str")
#     print("type of str",type(str))
###################################################
# dict = {101: "Krishna", 102: "Radha", 103: "Madhav"}
# print("dict items", dict)
# print("dict", dict)
# print("dict key", dict.keys())
# print("dict values", dict.values())
# print("dict keys and values", dict.keys(), dict.values())
# for key in dict.keys():
#     print("key is ", key)

# for value in dict.values():
#     print("value is ", value)
# for i, j in dict.items():
#     print(f"key is {i} and value is {j}")
#     print('key and value is', {i}, {j})

# ls = [3, 4, 5, 6]
# for i in ls:
#     print("ls before product ", ls)
#     ls[0] = ls[0] * ls[0]
#     ls[1] = ls[1] * ls[1]
#     ls[2] = ls[2] * ls[2]
#     ls[3] = ls[3] * ls[3]
#     print("ls after product", ls)

# print("list before square", ls)
# ls[0] = ls[0] * ls[0]
# ls[1] = ls[1] * ls[1]
# ls[2] = ls[2] * ls[2]
# print("list after square", ls)
# ls = [3, 4, 5, 6]
# for i in ls:
#     print("list before square ", ls)
#
#     print(f"list after square", i * i)
# ls2 = [1, 2, 3, 4, 5, 6, 7]
# print("list before square", ls2)
# ls3 = []
# for i in ls2:
#     print(f"{i} * {i}", i * i)
#     ls3.append(i * i)
#     print("list after square", ls3)
# ls3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print if number is even number
# ls_odd = []
# ls_even = []
# for i in ls3:
#     if i % 2 == 0: # 1%2 ==0
#         print(f"i is even number", i)
#         ls_even.append(i)
#     else:
#         print(f"i is odd number", i)
#         ls_odd.append(i)
# age = [10, 20, 30, 15, 18, 35]
#
# eligible_count = 0
# non_eligible_count = 0
# for i in age:
#     if i >= 18:
#         print(f"{i} is eligible for vote")
#         eligible_count = eligible_count + 1
#         print(eligible_count)
#     else:
#         print(f"{i} is not eligible for vote")
#         non_eligible_count = non_eligible_count +1
#         print(non_eligible_count)

# r = range(1,10,2)
# r = range(1, 10)
# print ("type of r", type(r))
# print("r value is", r)
# import random
# for i in range(1,10):
#     print(r)
r = range(1,10,2)
print("type of r", type(r))
print("r value is", r)
import random

# for i in range(1,10,2):
#for i in range(110, 210, 3):
#for i in range(5, 100, 5):
for i in range(100, 1, -5):
    print(i)



"""this is to practice control_flows in python created by prashant"""

# ls = [1, 2, 3, 4]
#
# for i in ls:
#     print("the elements in i:", i)
#
# print("-" * 50)
##########################################################################

# t = (4, 5, 6)
# for element in t:
#     print("the values available in t", element)
#
# print("-" * 50)
##########################################################################

# str = 'Prashant'
# for i in str:
#     print("rhe character in the str :", i)
#
# str1 = 'P,r,a,s,h,a,n,t,@#!^%*&'
# for i in str1:
#     print("rhe character in the str1 :", i)
#
# print("-" * 50)
##########################################################################

dict = {101: 'prashant', 102: 'nivi', 103: 'deppa'}
# for i in dict:
#     print(i)
#
# for i in dict.values():
#     print(i)
#
# print("dict.items():", dict.items())
# print("dict :", dict)
# print("the key values is dict.key :", dict.keys())
# print("the values is dict.values :", dict.values())
#
# for i, j in dict.items():
#     print("dict.items() of i,j:",i, j)
#
# for i, j in dict:
#     print("dict of i,j:",i, j)

# for keys in dict.keys():
#     print("the dict_key is :", keys)
#
# for values in dict.values():
#     print("the dict_value is :", values)
#
# for key, values in dict.items():
#     print(f"the key {key} and values is {values}")
#
# for i, j in dict.items():
#     print(f"the key {i} and values is {j}")

# print("-" * 50)
##########################################################################

ls2 = [1, 2, 3, 4, 5]
print("list ls2 before square :", ls2)
ls3 = []
for i in ls2:
    print(f"{i}*{i} =", i * i)
    ls3.append(i * i)
print("list ls2 after square :", ls3)

print("-" * 50)
##########################################################################

# print even & odd number
ls4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("list of ls4 is:", ls4)
for i in ls4:
    if i % 2 == 0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")
print("-" * 50)

# print even & odd number

ls4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("list of ls4 is:", ls4)
ls4_even = []
ls4_odd = []
for i in ls4:
    if i % 2 == 0:
        print(f"{i} is even number")
        ls4_even.append(i)
    else:
        print(f"{i} is odd number")
        ls4_odd.append(i)

print("ls4_even :", ls4_even)
print("ls4_odd :", ls4_odd)

# ------------------------------------------------------

print("-" * 50)

for i in ls4:
    if i % 2 == 0:
        print(f"{i} is even number")

print("-" * 50)

for i in ls4:
    if i % 2 == 1:
        print(f"{i} is odd number")

# print("-" * 50)
##########################################################################

age = (12, 15, 16, 18, 21, 25)
print(age)
# eligible_count = 0
for vote in age:
    # print(vote)
    if vote >= 18:
        print(f"{vote} is eligible for voting")
    else:
        print(f"{vote} is not eligible for voting")

#--------------------------------------------------------------------

age = (12, 15, 16, 18, 21, 25)
eligible_count = 0
non_eligible_count = 0
for vote in age:
    if vote >= 18:
        print(f"{vote} is eligible for voting")
        eligible_count = eligible_count + 1
        # eligible_count += 1
    else:
        print(f"{vote} is not eligible for voting")
        non_eligible_count = non_eligible_count + 1
        # non_eligible_count += 1

print("eligible_count =", eligible_count)
print("non_eligible_count =", non_eligible_count)

print("-" * 50)
##########################################################################

# range
# r = range(1, 10, 1)
# print("the r type is :", type(r))
# print("the value of r is =", r)
# for i in range(1, 10, 1):
#     print("the range of i is :", i)

# for r in range(100, 110):
#     print("the range of r is :", r)

for r in range(110, 100, -2):
    print("the range of r is :", r)
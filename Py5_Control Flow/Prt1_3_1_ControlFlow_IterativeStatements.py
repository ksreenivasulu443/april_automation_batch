'''
Iterative statements: to execute a group of statements multiple times then we should go for Iterative statements.
Iterative Statements : for, while
'''

# for loop: execute block of code certain nuber of times
# for x in sequence :
#  body

ls = [1, 2, 3, 4]  # ==> [1, 4, 9, 16]

for i in ls:
    print("elements in i is", i)

for n in ls:
    print("elements in i is", n)
    print("this code is inside of the for loop")

print("out side of for loop")

print("-------------string--------------")
strs = "Soma shekar"
for j in strs:
    print("elements in j is", j)

print("-------------dictionary--------------")
dicts = {1:"Arun", 2:"Bharath"}

for keys in dicts:
    print("key print method 1:", keys)

for keys in dicts.keys():
    print("key print method 2:", keys)

for values in dicts.values():
    print("values is:", values)

print("dicts.items()", dicts.items()) # print in Tuple


for keys, values in dicts.items():
    print("key and value is:", keys, values)

print("-------------exponential--------------")
ls1 = [1, 2, 3, 4]
print("List before square", ls1)
ls1[0] = ls1[0]*ls1[0]
ls1[1] = ls1[1]*ls1[1]
ls1[2] = ls1[2]*ls1[2]
ls1[3] = ls1[3]*ls1[3]
print("List after square", ls1)

ls2 = [4, 5, 6, 7, 8]
ls3 = []
print("List 2 after square", ls2)
for s in ls2:
    print(f"{s} * {s}", s*s)
    ls3.append(s*s)
print("List 2 after square", ls3)


# Question
# list of numbers
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list1 = []
odd_list1 = []

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        print(f"{num} is even number", num, end="\n")
        even_list1.append(num)

    else:
        print(f"{num} is odd number", num, end="\n")
        odd_list1.append(num)
# print even & odd list
print("even_list1", even_list1)
print("odd_list1", odd_list1)


# find how many are eligible to vote in tuple
tpl = (10, 18, 25, 13, 48, 17, 56)
eligible_cnt = 0
not_eligible_cnt = 0

# iterating each number in tuple
for elg_age in tpl:
    if elg_age>=18:
        print(f"{elg_age} is eligible for vote")
        eligible_cnt = eligible_cnt+1

    else:
        print(f"{elg_age} is not eligible for vote")
        not_eligible_cnt = not_eligible_cnt+1

print("eligible_cnt is:", eligible_cnt)
print("not_eligible_cnt is:", not_eligible_cnt)


# Range data type

r = range(1, 10)
print(r)

for i in r:
    print(i)
print()
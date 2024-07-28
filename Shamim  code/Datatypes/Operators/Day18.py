for i in range(10):
    print("the value of i is", i)

for i in range(1, 10):
    print("the value of i is", i)

for i in range(4, 12, 2):  # it will step to 2 valuse
    print("the value of i is", i)

for i in range(5, 20, 3):  # it will step to 3 valuse(5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20)
    print("the value of i is", i)

for i in range(10, -1, 1):  # no out put because (10 start -1 end 1 is positive direction)
    print("the value of i is", i)
#########################################################
# Question: calculate a sum of all numbers from 1 to given number:
num = int(input("enter number:"))
sum = 0
for i in range(1, num + 1):
    sum = sum + 1
    print(f"sum of 1 to {num} is", sum)
#############################################################
# Calculate the sum of all odd number within given range

num1 = int(input("enter number:"))
sum = 0
for i in range(1, num1 + 1):
    if i % 2 != 0:
        sum = sum + 1
    print(f"sum of odd number 1 to {num1} is", sum)

#############################################
# print a multiplication table of given number
# 2*1 =2
# 2*2 =4
# 2*3 =6
# 2*4=8
num3 = int(input("enter number:"))
for i in range(11):
    s = num3 * i
    print(f"{num3} * {i} = {s}")

#############################################
# find the factorial of a given number (6! =6*5*4*3*2*1)
fact = 1
num4 = int(input("enter numver:"))
for i in range(1, num4 + 1):
    fact = fact * i
    print(f"factorial of {num}", fact)

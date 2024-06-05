 # write a program to calculate

# num = int(input("Enter the range end number:"))
# sum_rnum = 0
#
# for i in range(1, num+1):
#     sum_rnum = sum_rnum + i
#     print("iteration +", sum_rnum)
#
#
# print(sum_rnum)
#
# nu = int(input("Enter the range end number:"))
# print(sum(range(1, nu+1, 1)))


# sum of numbers
# 1 2 3 4 5 6 7 8 9
num1 = int(input("Enter the range end number:"))  # 4
sum_rnum1 = 0
for i in range(1, num1+1, 2):  # 1+3
    sum_rnum1 = sum_rnum1 + i
print("sum of numbers", sum_rnum1)

num2 = int(input("Enter the range end number:"))  # 4+1 =5
sum = 0
for i in range(1,num2+1):  # 1+3
    if i%2 != 0:
        sum = sum + i
    # print(i)
print(f"sum of odd numbers between 1 to {num2} is", sum)  # 4

# multiplication
num3 = int(input("Enter the range end number:"))  # 4
for i in range(1,11):  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    s = num3 * i
    print(f"{num3} * {i} = {s}")  # 4 multiplication
#
# # find the factorial of a given number
# # 4 != 4*3*2*1
# # 5 != 5*4*3*2*1
num4 = int(input("Enter the range end number:"))
fact = 1
for i in range(1, num4+1):
    fact =fact * i
    print(fact)
print(f"factorial of {num4}", fact)
#
#
# # pattern
# num5 = int(input("Enter the range end number:"))
#
# for i in range(1, num5+1):
#     for j in range(1, num5+1):
#         print(i, end=" ")
#     print()

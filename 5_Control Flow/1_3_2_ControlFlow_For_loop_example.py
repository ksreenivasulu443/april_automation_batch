 # write a program to calculate

num = int(input("Enter the range end number:"))
sum_rnum = 0

for i in range(1, num+1):
    sum_rnum = sum_rnum + i
    print("iteration +", sum_rnum)


print(sum_rnum)

nu = int(input("Enter the range end number:"))
print(sum(range(1, nu+1, 1)))


# sum of add number

num1 = int(input("Enter the range end number:"))
sum_rnum1 = 0
for i in range(1, num1+1, 2):
    sum_rnum1 = sum_rnum1 + i
print(sum_rnum1)

num2 = int(input("Enter the range end number:"))
sum = 0
for i in range(1,num2+1):
    if i%2 != 0:
        sum = sum + i
    # print(i)
print(f"sum of odd numbers 1 to {num2} is", sum)

# multiplication
num3 = int(input("Enter the range end number:"))
for i in range(1,11):
    s = num3 * i
    print(f"{num3} * {i} = {s}")

# find the factorial of a given number
# 4 != 4*3*2*1
# 5 != 5*4*3*2*1
num4 = int(input("Enter the range end number:"))
fact = 1
for i in range(1, num4+1):
    fact =fact * i
print(f"factorial of {num4}", fact)


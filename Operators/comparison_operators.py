"""This module file is create to practice python Comparison_operators and
   created by Prashant on 07/05/2024"""

# 1.Equal to (==): Checks if the values of two operands are equal.
# 5 == 5 returns True.
a = 10
b = 25
print("a==b then ",a==b)
print("a!=b then ",a!=b)


# 2.Not equal to (!=): Checks if the values of two operands are not equal.
# Example: 10 != 25 returns True.
a = 10
b = 25
print("a!=b then ",a!=b)
print("a==b then ",a==b)


# 3.Greater than (>): Checks if the left operand is greater than the right operand.
# Example: 7 > 3 returns True.
a = 10
b = 25
print("a>b then ",a>b)
print("a<b then ",a<b)
print("b>a then ",b>a)
print("b<a then ",b<a)


# 4.Less than (<): Checks if the left operand is less than the right operand.
# Example: 4 < 6 returns True.
a = 10
b = 25
print("a>b then ",a>b)
print("a<b then ",a<b)
print("b>a then ",b>a)
print("b<a then ",b<a)


# 5.Greater than or equal to (>=): Checks if the left operand is greater than or equal to the right operand.
# Example: 5 >= 5 returns True.
a = 10
b = 25
print("a>=b then ",a>=b)
print("a<=b then ",a<=b)
print("b>=a then ",b>=a)
print("b<=a then ",b<=a)


# 6.Less than or equal to (<=): Checks if the left operand is less than or equal to the right operand.
# Example: 3 <= 2 returns False.
a = 10
b = 25
print("a>=b then ",a>=b)
print("a<=b then ",a<=b)
print("b>=a then ",b>=a)
print("b<=a then ",b<=a)

source_count = 10
target_count = 11

if source_count == target_count: # 10 ==11 ( False
    print("count is matching and test cases is pass")
else:
    print("count is not matching and difference is ", source_count-target_count)

age = 12

if age>=18: # 19>=18
    print("eligible for vote")
else:
    print("not eligible")


name = 'Prashant'
age = 30

if age >= 30:
    print(name)
else:
    print("no_name")

if age > 30:
    print(name)
else:
    print("no_name")



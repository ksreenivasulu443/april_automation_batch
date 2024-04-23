"""This module file is create to practice python float datatypes
created by Sreeni on 04/23/2024
"""

count = 10.0

print("The value of count is", count)
print("Type of count is", type(count))
print("Memory address of count is", id(count))

count2 = 10

print("The value of count2 is", count2)
print("Type of count2 is", type(count2))
print("Memory address of count2 is", id(count2))

count3 = 120734517362546731254621.0

print("The value of count3 is", count3) # 1.2073451736254674e+23 --> 1.1.2073451736254674*10^23
print("Type of count3 is", type(count3))
print("Memory address of count3 is", id(count3))
#
count4 = 1.23e2  # ==> 1.23 * 10 ^2

print("The value of count4 is", count4)
print("Type of count4 is", type(count4))
print("Memory address of count4 is", id(count4))

count5 = 13.454765462534324234534534534535345345345345

print("The value of count5 is", count5)
print("Type of count5 is", type(count5))
print("Memory address of count5 is", id(count5))

print("functions available in float type",dir(count))
print("1.2.is_integer()", 1.2.is_integer())

print(f"the ceil value of {count5}", count5.__ceil__())
print(f"the ceil value of {count5}", count5.__floor__())


count_neg = -15.23

print("The value of count_neg is", count_neg)
print("Type of count_neg is", type(count_neg))
print("Memory count_neg of count5 is", id(count_neg))


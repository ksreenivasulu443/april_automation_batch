"""this file is created to practice python Comparison Operators (class 14
) Created by khushboo on 07/05/2024"""


a = 10  # ( = assignment operator)
b = 25
print("a==b", a == b )  # ( == comparison opearator)

print("a!=b", a != b )  # ( == comparison opearator)

print("a>b", a > b)

print("a<b", a < b)

print("a>=b", a >= b)

print("a<=b", a <=b)


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
ls1 = [1, 2, 3, 4, 5, 6, 8]

for item in ls1:
    print(item)

str = 'shamim'
for i in str:
    print("char available in ", i)

dict = {102: 'shamim', 103: 'rehan'}
for i in dict.values():
    print('i')
    print("dict.keys", dict.keys())
    print("dict.values", dict.values())

for key in dict.keys():
    print("key is", key)

for value in dict.values():
    print("value is", value)

for key, value in dict.items():
    print(f"key is {key} and value is {value}")

ls2 = [4, 5, 6, 7, 8, 9]
print("before print ls2 ", ls2)
ls3 = []
for i in ls2:
    print(f"{i}*{i}", i * i)
    ls3.append(i * i)
    print("befor print ls3", ls3)

ls4_odd = []
ls5_even = []
ls = [1, 2, 3, 4, 5, 6, 8]
for i in ls:  # for is iterative statement
    if i % 2 == 1:  # if else conditional statement
        print(f"{i} is even num")
        ls5_even.append(i)
    else:
        print(f"{i} is odd num")
        ls4_odd.append(i)

age = (18, 19, 20, 69)

for i in age:
    if i >= 18:
        print(f"{i}  is eligible for vote")
        non_eligibele_count += 1
    else:
        print(f"{i} is not eligible for vote")

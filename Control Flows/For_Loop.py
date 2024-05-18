
ls = [1,2,3,4]

for item in ls:
    print("Element is",item)

t = (4,5,6)
for element in t:
    print("Element available is:", element)

str = 'sandy'
for i in str:
    print("character is:", i)


dict = {1:'sandy', 2:'deep'}

for d in dict:
    print(d)

dict = {1:'Rakesh', 2:'Kiran'}

for a,r in dict.items():
    print(a,r)


ls2 = [4,5,6,7,8,9,10]
print("List before square", ls2)
ls3= []
for i in ls2:
    print(i*i)
    ls3.append(i*i)
print("List after square", ls3)


ls7 = [1,2,3,4,5,6,7,8,9,10]

for i in ls7:
    if i % 2 == 0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")


ls8 = [1,2,3,4,5,6,7,8,9,10]

ls_odd = []
ls_even = []

for i in ls7:
    if i % 2 == 0:
        print(f"{i} is even number")
        ls_even.append(i)
    else:
        print(f"{i} is odd number")
        ls_odd.append(i)

print(ls_odd)
print(ls_even)


age = (22,17, 16, 33,44,22,10)

eligible_count = 0
not_eligible_count = 0

for i in age:
    if i >=18:
        print(f"{i} is eligible to vote")
        eligible_count = eligible_count + 1
    else:
        print(f"{i} is not eligible to vote")
        not_eligible_count = not_eligible_count + 1

print(eligible_count)
print(not_eligible_count)

r = range(1,22)

for i in range(1,22):
    print(i)

Sandeep
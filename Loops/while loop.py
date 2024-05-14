#while condition:
# code
# i=0
# while i<10:
#     print(i)
#     i=i+1
# i=10
# while i>=0:
#     print(i)
#     i=i-1
# data=[10,20,30,40,50]
# i=0
# while i<5:
#     #print(i)
#     print(data[i])
#     i=i+1

# alternate code
# while i<len(data):
#     #print(i)
#     print(data[i])
#     i=i+1

# lst=['sree','raj','dee']
# i=0
# while i<len(lst):
#     if lst[i]=='raj':
#         print('found the word in list')
#         break
#     i=i+1

# for i in range(1,10):
#     if i==5:
#         break
#     else:
#         print(i)
data=[1,2,3,0,4,5]
# for i in data:
#     if i==0:
#         break
#     print(10/i)

# continue statement
num=10
for i in data:
    if i==0:
        continue
    print(f'i valuse is {i} and {num/i} is',num/i)

for j in range(1,10):
    pass
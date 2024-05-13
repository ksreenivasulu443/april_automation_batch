# """for will iterate the collection data type """
# ls=[1,2,3,4]
#
# for item in ls:
#     print(f'all {item} in ls',item)
#
# t=(4,5,6,7)
# for element in t:
#     print(f'all {element} in t',element)
#     print('this print is inside the loop')
# print('this print is outside the loop')
#
# #string type
# str='sreeni'
# for character in str:
#     print(f'display each {character} in str',character)
#
# #dictionary
# dict={101:'sreeni',102:'raj'}
# print('all keys',dict.keys())
# print('all values',dict.values())
# for word in dict.values():
#     print(f'all {word} in dict',word)
# for i,j in dict.items():
#     print(f'all key and value in dict', i,j)
#
# for key in dict.keys():
#     print(key)
# for value in dict.values():
#     print(value)
# for key,value in dict.items():
#     print(f'key is {key}  and it is value {value}')

# ls2=[2,3,4,5,6,7,8]
# ls3=[]
# print('before square',ls2)
# for i in ls2:
#     print(f'square of ls2 {i}*{i}',i*i)
#     ls3.append(i*i)
# print('after square ls2',ls3)

#print if number is even
# ls4=[1,2,3,4,5,6,7,8,9,10]
# for j in ls4:
#     if j % 2==0:
#         print('even',j)
#     else:
#         print('odd', j)

# ls5=[1,2,3,4,5,6,7,8,9,10]
# ls_even=[]
# ls_odd=[]
# for a in ls5:
#     if a % 2==0:
#         ls_even.append(a)
#
#     else:
#         ls_odd.append(a)
#
# print(ls_even)
# print(ls_odd)
age=(18,20,17,22,34,16)
# for i in age:
#     print(i)
#     if i>=18:
#         print('eligible for vote',i)
#     else:
#         print('not eligible for vote', i)
#
eligible_count=0
for j in age:
    print(j)
    if j >= 18:
        print('eligible for vote', j)
        eligible_count=eligible_count+1
    else:
        print('not eligible for vote', j)
print('eligible count',eligible_count)


"""this module is created to practice while loop"""
# while condition:
#     code

# i=10
# while i>0:
#     print(i)
#     i = i-1


# for i in range(1,10):
#     if i == 5:
#         pass
#     print(i)
#
# data = [10, 20, 30, 40, 50]


# i = 4
# while i < len(data):
#     #print(i)
#     print(data[i])
#     i += 1
# print("outside while loop")
#
# list2 = ['apple','banana','mango']
# i=0
# while i < len(list2):
#     if list2[i] == 'apple':
#         print("Apple is found and search is complete")
#         break
#     i = i+1







# for i in data:
#     print(i)


#
# string = '!s,r,e,476327854@e,n,i'
# index = 0
# while index < len(string):
#     print("character in str:", string[index])
#     index += 1
#
# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(f"{i}*{j} = {i*j}")
#         j += 1
#     i += 1
#
#



#
#
#
# import sys
#
# balance = 0
# while True:
#     print('d-Deposit \nw-Withdraw \ne-exit')
#     option = input('Choose your option:')
#     if option.lower() == 'd' :
#         amt = float(input('Enter amount:'))
#         balance = balance + amt
#     elif option.lower() == 'w' :
#         amt = float(input('Enter amount:'))
#         if balance >= amt:
#             print("withdraw is in progress pls wait")
#             print("withdraw ampunt ")
#             balance = balance - amt
#         else:
#             print("do not have sufficient balance in account")
#     elif option.lower() == 'e' :
#         print("Do you want display balance on screen?")
#         option = input('Choose your option Y/YES:')
#         if option.lower() == 'y' :
#             print("balance is", balance)
#         else:
#             print('Thanks for Banking')
#         sys.exit()
#     else:
#         print('Invalid option..Plz choose valid option')

list = [1,2,3,4,5,0]


for i in range(1,10):
    if i == 5:
        print("i became 5 and program will be terminated")
        break
    else:
        print(i)

data = [1,2,3,4,5,0,6,7,0,8]

# for i in data:
#     if i ==0:
#         break
#     print(10/i)
#
# print("this is outside for loop")

num=10
for i in data:
    if i == 0:
        continue
    print(f"i value is {i} and {num}/{i}", num/i)

for i in range(1,10):
    pass
    print("hello this after pass")

print("hello this after pass")

def fun():
    pass
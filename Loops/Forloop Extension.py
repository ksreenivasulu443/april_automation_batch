# code to sum all numbers from 1 for given numbers
#range(star:end value:step:)
#star --optional
#end--optional
#step--optional
#but atleas one value should be given in the range
#end=end-1

# for i in  range(10):
#     print(f'number from range 10',i)
#

# num=int(input('enter number'))
# sum=0
# for i in range(1,num+1):
#     #print(i)
#    #sum=sum+i
#    sum=sum+i
#  #print(sum(range(1, num + 1, 1)))
#
# print('sum of all the given numbers',sum)

#print sum of oodd numbers in a given range

# for i in range(1,num+1):
#     if num % 2 !=0:
#         sum=sum+i
#         print('sum of odd number',sum)
# print the tables for specified number
# for i in range(1,11):
#     s=num*i
#     print(f'{i} * {num}=',s)
# tables from 1-10
# for i in range(1,11):
#     for j in range(1,11):
#         s=i*j
#         print(f'{i} * {j}=', s)

#Factorial of N
# number=int(input('enter number'))
# fact=1
# for i in range(1,number+1):
#      fact=fact*i
#
# print(f'factorial of {number}',fact)

#print * in Triangle

# for i in range(10):
#      print('*'*i)

# n=int(input('enter number'))
# for i in range(1,n+1):
#      for j in range(1,n+1):
#           print(i,end='  ')
#      print(i, end='\n')
# 1 2 3 4 ...
n=int(input('enter number'))
for i in range(1,n+1):
     for j in range(1,n+1):
          print(j,end='  ')
     print(i, end='\n')
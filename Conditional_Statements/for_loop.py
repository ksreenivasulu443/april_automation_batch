# FOR LOOP
# ls=[1,2,3,4]
# for item in ls:
#     print(item)

# t=(4,5,6)
# for  element in t:
#     print(element)
# #
# dict={1:"ETL",2:"Big Data"}
# for i in dict:
#     print(dict)
#
# dict={1:"ETL",2:"Big Data"}
# for key in dict.keys():
#     print(key)
#
# for value in dict.values():
#     print(value)
#
# ls2=[4,5,6,7,8,9,10]
# print(ls2)
# ls3=[]
# for i in ls2:
#     print(f"{i}*{i}",i*i)
#     ls3.append(i*i)
# print(ls3)

#########################################

#
# ls=[1,2,3,4,5]
# print(ls*2)
# ls[0]=ls[0]*ls[0]
# ls[1]=ls[1]*ls[1]
# ls[2]=ls[2]*ls[2]
# ls[3]=ls[3]*ls[3]
# ls[4]=ls[4]*ls[4]
# print("list of square is:",ls)
# #
# for i in ls:
#     print("ls square is:",ls)

########################################
#
# ls=[1,2,3,4,5,6]
# for i in ls:
#     print(i)
# if i%2==1:
#     print(f"{i} is even")
# else:
#     print(f"{i} is odd")
#
# ####################################################
#
# ls=[5,4,3,2,1]
# # print("list before square is:",ls)
# ls_sq=[]
# for i in ls:
#     ls_sq.append(i**2
#                  )
# print(ls_sq)

###############################################################

# ls=[5,4,3,2,1]
# # print("list before square is:",ls)
# ls_sq=[]
# for i in ls:
#     ls_sq.append(i**i)
# print(ls_sq)

############################################
# ls=[]
# for i in range(10):
#     ls.append(i)
# print(ls)
###########################################
# ls=[]
# for i in range(10,-1,-1):
#     ls.append(i)
# print(ls)
##############################################
# num=int(input("enter number:"))
# sum=0
# for i in range(1,num+1):
#     if i%2==0:
#     # print(i)
#         sum=sum+i
# print(sum)

#################################################

# sum of odd nums in a given range
#
# for i in range(1,10):
#     print(i)
#     sum=sum+i
# print(sum)

##########################################
#
# num=int(input("enter number:"))
# sum = 0
# for i in range(1,num+1):
#     if i%2 != 0:
#             sum = sum + i
#     # print(i)
#
# print(f"sum of odd numbers 1 to {num} is", sum)

#################################################
#
# fact=1
# num=int(input("enter a num:"))
# for i in range(1,num+1,):
#     fact=fact*i
#     print(fact)
#
##################################

# for i in range(1,5):
#     print(i)
#     for j in range(5,8):
#         print(j)
#         for k in range(8,11):
#             print(k)

######################################
#
# for i in range(0,5):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print("\n")

###############################################
# a=1
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(a,end=" ")
#     print("\n")

################################################

# a=1
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(a,end=" ")
#         a=a+1
#     print("\n")

##############################################

for i in range(1,6):
    print("*"*i)


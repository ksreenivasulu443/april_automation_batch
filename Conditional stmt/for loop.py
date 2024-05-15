#For loop practice
#syntax for element in colllection data types/string type

# ls=[1,2,3,4]
# for item in ls:
#     print("element is:",item)

# t = (1,2,3)
# for element in t:
#     print("the value avaliable is",element)
# print("outside of for loop")
#
# str='basha'
# for i in str:
#     print("print string elements",i)

# str="!s,r,e,123456@,n,i"
# for i in str:
#     print("char's in str",i)

# dict = {101,'basha',102,'sameer'}
#
# print("dict.items",dict.items())
# print("dict",dict)
# print("dict keys",dict.keys())
# print("dict values",dict.values())
#
# for key in dict.keys():
#     print("print keys")
# for value in dict.value():
#     print("print value")
# for i,j in dict.items():
#     print(i,j)


# ls2=[4,5,6,7,8,9,10]
# print("list before square",ls2)
# ls3=[]
# for i in ls2:
#     print(f"{i}*{i}", i *i )
#     ls3.append(i * i)
# print("list after square",ls3)

#print if the num is even number
#
# ls4 =[1, 2, 3, 4, 5, 6]
# ls_odd=[]
# ls_even=[]
#
# for i in ls4:
#     if i % 2 == 0:
#        print(f"print {i} even number")
#        ls_even.append(i)
#     else:
#        print(f"print {i} odd number")
#        ls_odd.append(i)
# print("odd_value",ls_odd)
# print("even_value",ls_even)

age=[1,18,25,77,99,17,69]
eligible_count=0
non_eligible_count=0

for i in age:
    if i >=18:
        print(f"{i} eligible for vote")
        eligible_count=eligible_count+1
    else:
        print(f"{i} not eligible for vote")
        non_eligible_count +=1

print("elegible count",eligible_count)

print("non-elegible count",non_eligible_count)


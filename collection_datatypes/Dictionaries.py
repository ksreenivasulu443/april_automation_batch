# FOR LOOP #
# for element in datatype/stringtype
#
# ls=[1,2,3,4]
# for element in ls:
#     print(element)
###########################################
#
# tp=(5,6,7,8)
# for element in tp:
#     print(element)
#
#################################################

# t=(4,5,6)
# for element in t:
#     print("the value is element",element)
#     print("this code is inside for loop")
#     print("hello this is for loop")
# print("outside loop")

###################################################

# str="Data Engineering"
# for i in str:
#     print(i)

#################################################

# dict={1:"ETL",2:"DE"}
# print(dict.items())
# print("dict",dict)
# print("Keys",dict.keys())
# print("values",dict.values())
#
# for key in dict:
#     print("keys:",dict.keys())
#
# for value in dict:
#     print("values:",dict.values())
#
# for i,j in dict.items():
#     print(i,j)

############################################
#

#########################################

#######################################
# --even or odd--
# ls_eo=[1,2,3,4,5,6,7,8,9,0]
# ls_even=[]
# ls_odd=[]
# for i in ls_eo:
#     if i%2==0:
#         print(f"{i} is even no")
#         ls_even.append(i)
#
# for i in ls_eo:
#     if i%2==1:
#         print(f"{i} is odd no")
#         ls_odd.append(i)
# print(ls_even)
# print(ls_odd)
#
# lso=[]
# for i in ls_eo:
#     if i%2==1:
#         print("odd no",i)
#         lso.append(i)
# print("odd:",lso)
#
# lse=[]
# for i in ls_eo:
#     if i%2==0:
#         print("even no",i)
#         lse.append(i)
# print("even:",lse)
# print("odd:",lso)

#######################################
# eligible_count=0
# not_eligible_count=0
# e_count=[]
# ne_count=[]
# age = (10,24,17,35,90,76)
# for i in age:
#     if i>=18:
#         print(f"{i} is eligible for vote")
#         eligible_count=eligible_count+1
#         e_count.append(i)
#         # ne_count.count(i)
#     else:
#         print(f"{i} is not eligible for vote")
#         not_eligible_count=not_eligible_count+1
#         ne_count.append(i)
#         # ne_count.count(i)
#
# print("age eligible for voting",e_count)
# print("age not eligible for voting",ne_count)

###################################################
#
# x = (10,20,30,40,50)
# for var in x:
#     print("index "+ str(x.index(var)) + ":",var)

#################################################
# stocks = {
#         'AAPL': 187.31,
#         'MSFT': 124.06,
#         'FB': 183.50
#     }
#
# for key, value in stocks.items() :
#     print(key + " : " + str(value))
#     print(stocks.keys())
#     print(stocks.values())
#
# print(stocks.values())

############################################
# direct & indirect reporting manager
#
# Input = {'A': 'A', 'B': 'A', 'C': 'B', 'D': 'B', 'E': 'D', 'F': 'E'}
# print(Input)

###################################################
#
# numbers=[1,2,3,4,5,0,9,8,7,6]
# print(numbers)
# even_no=list(filter(lambda x: x%2==0,numbers))
# odd_no=list(filter(lambda x: x%2==1,numbers))
# print("even_no:",even_no)
# print("odd_no:",odd_no)

####################################################
#
# squares = []
# for i in range(1,10,2):
#     squares.append(i**2)
# print(squares)
#
# square_list = [(lambda x: x*x)(x) for x in range(1,10,2)]
# print(square_list)

###########################################################

# from functools import reduce
#
# words = ["apple", "banana", "orange", "apple", "grape", "banana"]
#
# # Count the occurrences of each word
# word_counts = reduce(lambda counts, word: {**counts, word: counts.get(word, 0) + 1}, words, {})
#
# print(word_counts)
# # Output: {'apple': 2, 'banana': 2, 'orange': 1, 'grape': 1}


#####################################################################




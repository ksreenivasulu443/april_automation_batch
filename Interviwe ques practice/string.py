# # # # // 1. write a function to reverce a given string//
# # # txt = "Hellow World"
# # # print("original string", txt)
# # # print("reverse String", txt[: : -1])
# # #
# # # txt = "Radha Krishna"[: : -1]
# # # print(txt)
# # #
# # # def my_function(txt):
# # #     return txt[: : -1]
# # # mytxt = my_function("Radha Radha Radha")
# # # print(mytxt)
# # #
# # # Write a function to count the number of occurrences of a specific character in a string.
# # # Native maethod :
# # # initializing string
# # test_str = "GeeksforGeeks"
# #
# # # using naive method to get count
# # # counting e
# # count = 0
# #
# # for i in test_str:
# # 	if i == 'e':
# # 		count = count + 1
# #
# # # printing result
# # print("Count of e in GeeksforGeeks is : "
# # 	+ str(count))
# #
# # str1= "Radha Radha Radha"
# # count = 0
# # for i in str1:
# #     if i == 'a':
# #         count = count+1
# #
# # print("count of a in given string is :" +str(count))
#
# # initializing string
# test_str = "GeeksforGeeks"
#
# # using count() to get count of "e"
# counter = test_str.count('e')
#
# # printing result
# print("Count of e in GeeksforGeeks is : " + str(counter))
#
# str1 = "radha radha radha radha radha"
# count = str1.count('r')
# print("count of r in given string is "+ str(count))
# print("count of a in given string", str1.count('a'))
#
# string = "i love my life always"
# count = 0
# for i in string:
#     if i == 'l':
#        count = count + 1
# print( "count of 'l' char in given string ", str(count))
#
# print("count of 'l' char in given string ", string.count('l'))
#
# # function which return reverse
#
# def ispalindrome(s):
#     return s == s[::-1]
#
# s = "malayalam"
# ans = ispalindrome(s)
# if ans :
#  print("YES")
# else:
#  print("NO")
#
# def isPalindrome(s):
#     return s == s[::-1]
#
#
# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)
#
# if ans:
#     print("Yes")
# else:
#     print("No")
#----------------------------------------------------------------------------------------

string = input("Enter String:")
print("original string", string)
vowels = ['a', 'e','i', 'o', 'u', 'A', 'E', 'I','O', 'U']
result =""
for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]
print("After removing Vowels: ", result)



string = input("Enter Input: ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for char in string:
    if char not in vowels:
        result = result + char

print("\nAfter removing Vowels: ", result)








#
#

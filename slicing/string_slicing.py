"""This module file is create to practice python string slicing
created by Sreeni on 04/29/2024
"""

str = 'ETL'

print("str value is ", str)
 # Python index starts from 0
 # python index end value is len(str)-1
 # to slice any iterative data(str, list, tuple, df, array, etc) using python we have to use square brackets []

 # syntax to slice iterative data : str[start pos : end pos : step],
# start pos is mandatory, end pos - optional, step - optional, default step value is +1

print(f"first character available in {str} is : ", str[0])
print(f"second character available in {str} is : ", str[1])
print(f"third character available in {str} is : ", str[2])
print(f"In {str} first character available is {str[0]}, second character is {str[1]}, and third character {str[2]}   ")
#print(f"fourth character available in {str} is : ", str[6])

# for i in range(len(str)):
#     print(f"the value at index {i} value is", str[i])

str = 'ETL AUTOMATION'
print(f"0:6 characters available in {str} is : ", str[0:6]) # end = end-1 , str[0 to 5 character]
print(f"0:2 characters available in {str} is : ", str[0:2]) # end = end-1 , str[0 to 1 character]
print(f"str[5:] characters available in {str} is : ", str[5:])
print(f"str[:5] characters available in {str} is : ", str[:5])


email= 'seenu@gmail.com'

print(f"user from {email}", email[email.find('@')+1:])

print("str.find('A')", str.find('A'))
print("str.rfind('A')", str.rfind('A'))

print(f"str[::2] characters available in {str} is : ", str[::3])

print(f"str[2:10:1] characters available in {str} is : ", str[2:10:1]) # start 2, end = 10-1 =9 2 to 9

print(f"str[2:10:1] characters available in {str} is : ", str[2:10:2]) # start 2, end = 10-1 =9 2 to 9

print(f"str[2:10:3] characters available in {str} is : ", str[2:10:3])








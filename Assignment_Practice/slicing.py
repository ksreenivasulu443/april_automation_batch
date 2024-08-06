# Slicing

# Positive_Index

# str = 'ETL'
# print('the values of str :', str)
#
# print("find the first_character available in the given str :", str[0])
# print("find the second_character available in the given str :", str[1])
# print("find the third_character available in the given str :", str[2])
# # print("find the character available in the given str :", str[3]) # IndexError: string index out of range
#
# print("*" * 70)
#
# print(f"find the first_character available in the given {str} :", str[0])
# print(f"find the second_character available in the given {str} :", str[1])
# print(f"find the third_character available in the given {str} :", str[2])
#
# print("*" * 70)
#
# for i in range(len(str)):
#     print(f"the value of index {i} is : ", str[i])
#
# str_1 = 'ETL AUTOMATION'
# print(f"find the 0 to 4 available in the given {str_1} :", str_1[0:4])
# print(f"find the 0 to 6 available in the given {str_1} :", str_1[0:6])
# print(f"find the 0 to 2 available in the given {str_1} :", str_1[0:2])
# print(f"find the 0 to 1 available in the given {str_1} :", str_1[0:1])
# print(f"find the 0  available in the given {str_1} :", str_1[0:])
# print(f"find the 0 to 1 available in the given {str_1} :", str_1[0:1])
# print(f"find the 1 to 6 available in the given {str_1} :", str_1[2:6])
# print(f"find the 0 to 1 available in the given {str_1} :", str_1[:])
# print(f"find the 0 to 1 available in the given {str_1} :", str_1[:3])

# name = 'Prashant'
# print(f"find the first_charterer from {name} : ", name[0])
# print(f"find the first_charterer from {name} : ", name[0:3])
# print(f"find the first_charterer from {name} : ", name[0:5])
#
# email = 'etldev2023@gmail.com'
# print(f"user_name from {email} is : ", email[0:email.find('@')])
# print(f"user_name from {email} is : ", email[email.find('@'):])
# print(f"user_name from {email} is : ", email[email.find('@') + 1:])

# mail = 'prashantdc012@gmail.com'
# print(f"print the user name from given {mail} :", mail[0:mail.find('@')])
# print(f"print the domain name from given {mail} :", mail[mail.find('@'):])
# print(f"print the service_provider name from given {mail} :", mail[mail.find('@')+1:])

# step position
print("#step position")
print("=" * 100)

# str_2 = 'ETL AUTOMATION'
# print(f"{str_2} : ",str_2[0:10:1])
# print("slicing of str_2 is : ",str_2[2:10:1])
# print("slicing of str_2 is : ",str_2[2:10:2])
# print("slicing of str_2 is : ",str_2[1:13:3])
# print("slicing of str_2 is : ",str_2[1:13:2])
# print("slicing of str_2 is : ",str_2[1:5:2])
# print("slicing of str_2 is : ",str_2[0 : :2])
# print("slicing of str_2 is : ",str_2[::])
# print("slicing of str_2 is : ",str_2[::1])
# print("slicing of str_2 is : ",str_2[::2])


# str_3 = 'Prashant Chajagoud'
# print(f"{str_3} is : ", str_3[0])
# print(f"{str_3} is : ", str_3[0:])
# print(f"{str_3} is : ",str_3[0::])
# print(f"{str_3} is : ",str_3[0:1])
# print(f"{str_3} is : ",str_3[0:1:1])
# print(f"{str_3} is : ",str_3[0:18:1])
# print(f"{str_3} is : ",str_3[0:18:2])
# print(f"{str_3} is : ",str_3[0:18:3])

print("*"*60)

str_4 = 'prashant91@gmail.com'
print(f"print the usr name from {str_4} is :", str_4[0:str_4.find('@')])
print(f"print the usr name from {str_4} is :", str_4[str_4.find('@'):])
print(f"print the usr name from {str_4} is :", str_4[str_4.find('@')+1:])



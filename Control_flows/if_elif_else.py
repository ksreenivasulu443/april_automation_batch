"""this file is created to practice python if_elif_else (class 15 &16)
Created by khushboo on 08/05/2024"""

"""this file is created to practice if-elif-else"""

# if
# if-elif
# if-elif-else
# if-else

##############################################
# Syntax for if

# if condition:
#     code
# name = """Sreeni"""
# # name = input("enter name:")
# if name == '''Sreeni''':
#     print("this is inside if statement")
#     print(f"hello {name}, good morning")
#
# print("This is outside if statement")

##############################################

# Syntax: if-elif
# if condition:
#     code
# elif condition:
#     code

# name = 'sreeni'
# name = input("enter name:")
# if name == 'Sreeni' :
#     print("this is inside if statement")
#     print(f"hello {name}, Good morning")
# elif name=='Sreeni' :
#     print("this is inside elif statement under Raghav")
#     print(f"hello {name}, Good morning")
# elif name == 'Sudheer':
#     print("this is inside elif statement under Sudheer ")
#     print(f"hello {name}, Good morning")
#
# print("This is outside if statement")
##############################################


# sytax : if-elif-else
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

# name = input("enter name:")
# if name == 'Sreeni':
#     print("this is inside if statement")
#     print(f"hello {name}, Good morning")
# elif name == 'Raghav':
#     print("this is inside elif statement under Raghav")
#     print(f"hello {name}, Good morning")
# elif name == 'Sudheer':
#     print("this is inside elif statement under Sudheer ")
#     print(f"hello {name}, Good morning")
# else:
#     print("Hello Guest, Good morning")
#
# print("this is outside")
# print("this is outside 2")


# 0-Zero, 1-One, 2-two,3 - three, ...10-ten
#
# number = int(input("enter number:"))
# print("type of number", type(number))
#
# if number==0 :
#     print("entered number is Zero")
# elif number == 1:
#     print("entered number is one")
# elif number == 2:
#     print("entered number is two")
# elif number == 3:
#     print("entered number is three")
# elif number == 4:
#     print("entered number is four")
# elif number == 5:
#     print("entered number is five")
# elif number == 6:
#     print("entered number is six")
# elif number == 7:
#     print("entered number is seven")
# elif number == 8:
#     print("entered number is eight")
# elif number == 9:
#     print("entered number is nine")
# elif number == 10:
#     print("entered number is ten")
# else:
#     print("entered number is not between 0 and 10, please retry")

# take a number using input method and
# print if num>0 as positive number,
# elif number = 0 print as zero
# else negative number

# take age using input method and
# print if age>=18 as eligible for vote
# else print not eligible and you will be eligible for vote in x years ( x should 18-entered age)

# take marks using input method
# print if marks>=70 as Grade A
# print if marks between 60 and 70 Grade B
# print if marks between 50 and 60 Grdae C
# print if marks between 40 and 50 Grdae D
# else failed










# age = 12  # int(input("enter age:"))
#
# if age > 18:
#     print("Eligible for vote")
# else:
#     print("Not eligible")
#     eligible_for_vote_in_years = 18 - age
#     print("you will be eligible for vote in ", eligible_for_vote_in_years, "years")
#
# number = 10
#
# if number > 0:
#     print("number is positive")
# else:
#     print("number is negative")
#
# age = 25
#
# # Transform age category
# if age < 25:
#     category = "Young"
# elif 25 <= age < 30:
#     category = "Middle-aged"
# else:
#     category = "Elderly"
#
# print(f"Age: {age}, Category: {category}")
#
# marks = 55
#
# if marks>=70:
#     print("Grade A")
# elif 60 <= marks < 70:
#     print("Grade B")
# elif 50 <= marks < 60:
#     print("Grade C")
# elif 40 <= marks < 50:
#     print("Grade D")
# else:
#     print("Fail")
#
# str1 = "sreeni"
# print("reverese string", str1[::-1])
# rev_str= str1[::-1]
#
#
# if str1 == rev_str:
#     print("palindrome")
# else:
#     print("not palindrome")

# num = '1bb1'
# print("type of num", type(num))
# num = str(num)
# rev_num = num[::-1]
# print("rev_num", rev_num)
#
# if num == num[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


#
# #count, file_read, positive or negative
#
# a = 10
# b = 10
# c = -10
# if a > 0 and b > 0:
#     print("The numbers are greater than 0")
# if a > 0 and b > 0 and c > 0:
#     print("The numbers are greater than 0")
# else:
#     print("Atleast one number is not greater than 0")
#
#
#
#
# # Python program to demonstrate
# # logical and operator
# a = 10
# b = 12
# c = 0
# if a and b and c:
#     print("All the numbers have boolean value as True")
# else:
#     print("Atleast one number has boolean value as False")
#

#etl project , source count, target

source_count = 10
target_count = 9
if source_count == target_count:
    print("count is matching")
else:
    print("count is not matching and difference is", abs(source_count-target_count))


#files--> csv, text, json, avro, parquet, table(oracle, mysql, sqlserver, post, snow)
file_type = input("enter file type:")
header = False
if file_type == 'csv':
    print("code to read csv file")
    if header :
        print("code will read csv file with header")
    else:
        print("code will read csv file without header")
elif file_type == 'json':
    print("code to read json file")
elif file_type == 'parquet':
    print("code to read parquet file")
else:
    print("entered format is not handled")
"""this is to practice control_flows in python"""

# import code

# syntax
# if
# if-elif
# if-elif-else
# if-else
##################

# if statement
# syntax
# if condition:
#     code
# ----------------

# name = "Prashant"
name = input("enter name")
if name == "Prashant":
    print("this is inside if statement")
    print(f"hello {name},good morning")

print("this is outside if statement")

place = "Belagavi"
place = input("enter the place :")
if place == 'Belagavi':
    print("this place is in the karnataka")
    print(f"Namma {place}")

print("it is not in karnataka")

name = 'Chikodi'
name = input("enter the name :")
if name == 'Chikodi':
    print("this place is in belagavi")
    print(f"{name} is a small town in belagavi")
print("it is not in Belagavi")

name = input("enter the name :")
if name == "Nivi":
    print("It is in the list")
    print(f"hi {name}")

print("It is not in the list")

####################################################

# if-elif
# syntax
# if condition:
#     code
# elif condition:
#     code
# ----------------------

name = "Prashant"
name = input("enter name :")
if name == "Prashant":
    print("this is inside if statement")
    print(f"hello {name},good morning")
elif name == "Nivi":
    print("this is inside if statement")
    print(f"hello {name},good morning")
elif name == "Shruti":
    print("this is inside if statement")
    print(f"hello {name},good morning")
else:
    print("this is outside if statement")

###################################################################


# else
# syntax
# if condition:
#     code
# elif condition:
#     code
# else:
#     code
# ------------------------

name = input("Enter the name:")
if name == "Prashant":
    print("He is ETL Automation april_batch student")
    print(f"Well_come to ETL classes {name}")
elif name == "Babalu":
    print("He is ex-student of sreeni class")
    print(f"thank you attending the class {name}")
elif name == "Shree":
    print("ETL Automation Trainee")
else:
    print("He is not april_batch student")

######################################################################

# 0-Zero, 1-One, 2-Two, 3-Three, 4-four, --------,10-Ten
number = input("Enter number :")
print("type o number",type(number))

number = int(input("Enter number :"))

if number == 0:
    print("the entered number is Zero")
elif number == 1:
    print("the entered number is One")
elif number == 2:
    print("the entered number is Two")
elif number == 3:
    print("the entered number is Three")
elif number == 4:
    print("the entered number is Four")
elif number == 5:
    print("the entered number is Five")
elif number == 6:
    print("the entered number is Six")
elif number == 7:
    print("the entered number is Seven")
elif number == 8:
    print("the entered number is Eight")
elif number == 9:
    print("the entered number is Nine")
elif number == 10:
    print("the entered number is Ten")
else:
    print("Entered number is not between 1 to 10 pls retry")

###########################################################################

number = int(input("Enter number:"))
if number > 0:
    print("the positive number")
elif number == 0:
    print("the number is equal to zero")
else:
    print("The given number is negtive")


number = float(input("Enter number:"))
if number > 0:
    print("the positive number")
elif number == 0:
    print("the number is equal to zero")
else:
    print("The given number is negative")


age = float(input("enter age:"))
if age >= 18:
    print("eligible for vote")
elif age == 18:
    print("not eligible for vote")
else:
    print("You will eligible for voting after 18")


age = float(input("enter age:"))
if age >= 18:
    print("eligible for vote")
else:
    print("not eligible for vote")

# take marks using input method
# print if marks>=70 as Grade A
# print if marks between 60 and 70 Grade B
# print if marks between 50 and 60 Grdae C
# print if marks between 40 and 50 Grdae D
# else: failed

marks = float(input("Scored marks:"))
if marks >= 70:
    print("Scored grade A")
elif marks >= 60 and marks < 70:
    print("Scored grade B")
elif marks >= 50 and marks < 60:
    print("Scored grade C")
elif marks >= 40 and marks < 50:
    print("Scored grade D")
else:
    print("failed")

marks = float(input("Scored marks:"))
if marks >= 70:
    print("Scored grade A")
elif 60 <= marks < 70:
    print("Scored grade B")
elif 50 <= marks < 60:
    print("Scored grade C")
elif 40 <= marks < 50:
    print("Scored grade D")
else:
    print("failed")


age = float(input("Eligible for voting:"))
if age >= 18:
    print("Eligible or voting")
elif age+1==18:
    print("Eligible for voting after one year")
elif age+2==18:
    print("Eligible for voting after two year")
else:
    print("Not eligible or voting")


age = float(input("Age generation:"))
if age <= 1 and age < 12:
    print("Childhood")
elif age>=12 and age<=20:
    print("Teenage")
elif age>=20 and age<=50:
    print("Middle_age")
elif age>=50 and age<=70:
    print("Old_age")
else:
    print("Budda")


# palindrome
str1 = 1221
str2 = str(str1)
print("reverse of str1:",str2[::-1])
#
name = "Prashant"
print("the reverse name prashant =",name[::-1])

name = "Prashant"
print("reverse name of prashant :",name[::-1])
#
number = 7019679563
num = str(number)
print("reverse the phone_number :",num[::-1])

number = 1221
number = str(number)
rev_num = number[::-1]
if number == rev_num:
    print("1221 is a palindrome number")
else:
    print("1221 ia not a palindrome number")
#
number = 121
number = str(number)
rev_num = number[::-1]
if number == rev_num:
    print("121 is a palindrome number")
else:
    print("121 ia not a palindrome number")

number = 153
number = str(number)
rev_num = number[::-1]
if number == rev_num:
    print("153 is a palindrome number")
else:
    print("153 is not a palindrome number")


name = "Madam"
rev_names = name[::-1]
if name == rev_names:
    print("Madam is palindrome")
else:
    print("Madam is not palindrome")

name = "madam"
rev_names = name[::-1]
if name == rev_names:
    print("Madam is palindrome")
else:
    print("Madam is not palindrome")

state = 'malayalam'
rev_sta = state[::-1]
if state == rev_sta:
    print("malayalam is palindrome")
else:
    print("malayalam is not a palindrome")

state1 = 'belagavi'
rev_sta1 = state1[::-1]
if state1 == rev_sta1:
    print("belagavi is palindrome")
else:
    print("belagavi is not a palindrome")

num1 = '1bb1'
print("the type of 1bb1 is",type(num))
num = num1[::-1]
if num == num1:
    print("1bb1 is palindrome")
else:
    print("1bb1 is not palindrome")
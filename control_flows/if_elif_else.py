"""this is to practice control_flows in python"""

import code

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

name = "Prashant"
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

0-Zero, 1-One, 2-Two, 3-Three, 4-four, --------,10-Ten
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

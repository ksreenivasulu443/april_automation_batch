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

number = int(input("enter number:"))
print("type of number", type(number))

if number == 0:
    print("entered number is Zero")
elif number == 1:
    print("entered number is one")
elif number == 2:
    print("entered number is two")
elif number == 3:
    print("entered number is three")
elif number == 4:
    print("entered number is four")
elif number == 5:
    print("entered number is five")
elif number == 6:
    print("entered number is six")
elif number == 7:
    print("entered number is seven")
elif number == 8:
    print("entered number is eight")
elif number == 9:
    print("entered number is nine")
elif number == 10:
    print("entered number is ten")
else:
    print("entered number is not between 0 and 10, please retry")



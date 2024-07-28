num = 1
if num > 0: print("positive number")

number = int(input("enter a number"))
if number > 0:
    print("positive num2")
elif number == 0:
    print("o number")
else:
    print("negative number")

age = int(input("enter eligible for vote"))
if age > 18:
    print("your eligible for vote")
else:
    print("not eligible for vote")

age = int(input("enter eligible for vote"))
if age > 18:
    print("you can eligible for the vote")
elif age + 1 == 18:
    print("you can eligible for the vote in one yr")
elif age + 2 == 18:
    print("you can eligible for the vote in two yrs")
else:
    print("not elogible for the vote")

number = 1221
if number == str(number)[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# Assigment 1 MAX and MIN Int Value
import sys
int_max = sys.maxsize
print("Max Value of the integer is:",int_max)

int_min = -sys.maxsize
print("Minimum Value of the integer is:",int_min)

# Assignment 2 Convert Numerical string value into int
a = input("enter the integer number:")
print("Entered number is number ",type(a),a)
# to Convert into str number into integer
print("Str is converted to Int",type(int(a)),a)

# Assigment to print given number is even or odd

G_num = input("Enter any number")
G_num1 = int(G_num)
if (G_num1%2) == 0:
    print("Given number is even",G_num1)
if (G_num1%2) != 0:
    print("Given number is odd:",G_num1)

# Precision dealing with the python float number.
import sys
f_number = 3.4897879
print("The float number is as assigned",f_number)
print("To print the precision upto 2 decimal point",round(f_number,2))
print("to print the number upto 3 decimal point","{0:.3f}".format(f_number))

#


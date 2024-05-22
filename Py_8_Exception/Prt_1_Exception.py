'''
Exception Handling:
1. Syntax Errors(parentheses, :, condition assigning, quote) ,  Name Errors(inbuilt function )
 2. Runtime Errors
'''

# Syntax Errors ex:
# x=10
# if x==10
#  print("Hello")
# print("Hello"
# print("Hello)

# Name Errors ex:
# Print("Hello")
# num1 = Int(input("enter the number:"))
# print(num1)

try:
    a = int(input("enter the value of a :"))
    b = int(input("enter the value of b :"))

    sum1 = a + b
    sub = a - b
    mul = a * b
    div = a / b
    print(f"sum, sub, mul, div of {a} and {b}:", sum1, sub, mul, div)
# except:
#     print("error during calculation, please retry")

except ZeroDivisionError as e:
    print("ZeroDivisionError during calculation, please retry:", e)

except TypeError as e:
    print("TypeError during calculation, please retry:", e)

except ValueError as e:
    print("ValueError during calculation, please retry:", e)

except NameError as e:
    print("NameError during calculation, please retry:", e)

except (ZeroDivisionError, TypeError, ValueError, NameError) as e:
    print("Error during calculation, please retry:", e)
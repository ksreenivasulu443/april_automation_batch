# import timeit
#
# # Function to sum numbers using a for loop
# def sum_with_for_loop(n):
#     total = 0
#     for i in range(n):
#         total += i
#     return total
#
# # Function to sum numbers using a while loop
# def sum_with_while_loop(n):
#     total = 0
#     i = 0
#     while i < n:
#         total += i
#         i += 1
#     return total
#
# # Measure execution time for the for loop
# print("Time taken by for loop:", timeit.timeit(lambda: sum_with_for_loop(1000000), number=1))
#
# # Measure execution time for the while loop
# print("Time taken by while loop:", timeit.timeit(lambda: sum_with_while_loop(1000000), number=1))
#
#
# import timeit
#
# # Function to search for an element using a for loop
# def search_with_for_loop(lst, target):
#     for item in lst:
#         if item == target:
#             return True
#     return False
#
# # Function to search for an element using a while loop
# def search_with_while_loop(lst, target):
#     i = 0
#     while i < len(lst):
#         if lst[i] == target:
#             return True
#         i += 1
#     return False
#
# # Generate a large list of numbers
# lst = list(range(1000000))
#
# # Measure execution time for the for loop
# print("Time taken by for loop:", timeit.timeit(lambda: search_with_for_loop(lst, 1), number=1))
#
# # Measure execution time for the while loop
# print("Time taken by while loop:", timeit.timeit(lambda: search_with_while_loop(lst, 1), number=1))

#
# def greet(name):
#     "this is greet func"
#     return f"Hello, {name}!"
#
# # Call the function
# print(greet("Alice"))  # Output: Hello, Alice!
#
# print(greet.__name__)
#
# print(greet.__doc__)
#
# def add(a, b):
#     return a + b
#
# # Call the function
# result = add(3, 5)
# print(result)  # Output: 8
#
#
# def is_even(number):
#     return number % 2 == 0
#
# # Call the function
# print(is_even(4))  # Output: True
# print(is_even(7))  # Output: False
#
#
# def square(number):
#     return number ** 2
#
# # Call the function
# print(square(4))  # Output: 16
# print(square(7))  # Output: 49
#
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
#
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9
#
# # Call the functions
# print(celsius_to_fahrenheit(0))    # Output: 32.0
# print(fahrenheit_to_celsius(32))    # Output: 0.0
#
#
# def sum_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# # Calling the function with variable positional arguments
# print(sum_numbers(1, 2, 3))  # Output: 6
#
# a=10
# b=20
#
# print(a+b)
#
# a=30
# b=40
# print(a+b)
#
# a=40
# b=50
# print(a+b)
#
# def calc(a,b):
#     print(f"sum of a & b is", a+b)
#
# print(calc(10,20))
# calc(10,30)


# Global variable
global_var = "I'm a global variable"

def outer_function():
    outer_var = "I'm an outer variable"

    def inner_function():
        inner_var = "I'm an inner variable"

        # Print local namespace
        print("Local namespace (inner_function):", locals())

    # Print local namespace
    print("Local namespace (outer_function):", locals())

    # Call inner function
    inner_function()

# Print global namespace
print("Global namespace:", globals())

# Call outer function
outer_function()




def calc3(a, b, c, d):
    print("a value is ", a)
    print("b value is ", b)
    print(f"sum of two numbers", a + b)
    print(f"sub of two number", a - b)
    print(f"mul of two number", a * b)
    print(f"div of two number", a / b)
    return a + b, a - b, a * b, a / b

calc3(10,20,30,40)

def cal(*args,d=10):
    sum =0
    for i in args:
        sum=sum+i
    return sum,d

print(cal(20,50,300,100,d=100))

def cal2(**kwargs):
    sum=0
    for value in kwargs.values():
        sum=sum+value
    return sum

print(cal2(a=10,b=20))

def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)


1.	f(3,2) ==>	3 2 4  8

2.	f(10,20,30,40) ===>10 20 30 40
3.	f(25,50,arg4=100) ==>25 50 4 100

4.	f(arg4=2,arg1=3,arg2=4)===>3 4 4 2
5.	f()===>Invalid
TypeError: f() missing 2 required positional arguments: 'arg1' and 'arg2'

6.	f(arg3=10,arg4=20,30,40)	==>Invalid
SyntaxError: positional argument follows keyword argument
[After keyword arguments we should not take positional arguments]

7.	f(4,5,arg2=6)==>Invalid
TypeError: f() got multiple values for argument 'arg2'
8.	f(4,5,arg3=5,arg5=6)==>Invalid
TypeError: f() got an unexpected keyword argument 'arg5'




# Count occurrences of a character in a string:
# Find the maximum of three numbers:
# write python function to print factorial of numbers
# read two files and compare the count

# Count occurrences of a character in a string:
# string = 'Sreeni'
# string_char ='S'--1
#
# 1,2,3
#
# 4,5,6
# 14,15,12


import pandas as pd




def read_fun(path, file_type):
    print("i am reading data from :", path)
    if file_type=='csv':
        df = pd.read_csv(path)
    elif file_type =='excel':
        df= pd.read_excel(path)
    return df


source = read_fun('/Users/harish/PycharmProjects/april_automation_batch/python_function/source.csv','csv')
print(type(source))
print(source.head(3))
target = read_fun('/Users/harish/Documents/April batch/Notes/April_batch_class_excel_notes.xlsx', 'excel')
print(target.head(3))

r"/Users/harish/PycharmProjects/april_automation_batch/python_function/source.csv"


def count_check(source, target):
    source_count = source.shape[0]
    target_count = target.shape[0]
    if source_count == target_count:
        print(f"count is matching: source count is {source_count} and target count is {target_count}")
    else:
        print(f"count is not matching:  source count is {source_count}, target count is {target_count} and difference "
              f"is {source_count-target_count}")


count_check(source, target)


def data_compare(source, target):
    return source.compare(target)

print(data_compare(source, target))


# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i  # result = result * i
#     print(f"factorial of {n} is", result)
#     return result
#
#
# factorial(6)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# # Example usage:
# print(factorial(6))  # Output: 120
# factorial(6) calls factorial(5) * 6.
# factorial(5) calls factorial(4) * 5.
# factorial(4) calls factorial(3) * 4.
# factorial(3) calls factorial(2) * 3.
# factorial(2) calls factorial(1) * 2.
# factorial(1) calls factorial(0) * 1.
# factorial(0) returns 1 (base case).

# factorial(1) returns 1 * 1 = 1.
# factorial(2) returns 1 * 2 = 2.
# factorial(3) returns 2 * 3 = 6.
# factorial(4) returns 6 * 4 = 24.
# factorial(5) returns 24 * 5 = 120.

#
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

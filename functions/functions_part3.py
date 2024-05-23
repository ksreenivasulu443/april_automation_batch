# Count occurrences of a character in a string:
# Find the maximum of three numbers:
# write python function to print factorial of numbers
# read two files and compare the count
#
# #################Count occurrences of a character in a string:###########
#
# def count_occurences(string,char):
#     str_count=string.count(char)
#     print(str_count)
#     return str_count
# print(count_occurences("Babulu","l"))
#
# ############################APPROACH-2###################################
# def count_occurences(string,char):
#     str_count=string.count(char)
#     print(str_count)
#     return str_count
# string=input("enter string:")
# char=input("enter char:")
# count_char=string.count(char)
# print(count_char)
#
# ###################Find the maximum of three numbers:##############
# ############################APPROACH-1###################################
#
# def max_3_no(a,b,c):
#     maxno=max(a,b,c)
#     return maxno
# max=(max_3_no(10,20,30))
# print(f"max of 3 nos:",max)
#
# ############################APPROACH-2###################################
# def find_maximum(*numbers):
#     if len(numbers) == 0:
#         return None
#     else:
#         return max(numbers)
#
# # Take input from the user
# numbers_input = input("Enter numbers separated by spaces: ")
#
# # Split the input string into individual numbers
# numbers_list = [int(num) for num in numbers_input.split()]
#
# # Call the function with the numbers provided by the user
# maximum = find_maximum(*numbers_list)
#
# # Print the maximum number
# if maximum is not None:
#     print("Maximum number:", maximum)
# else:
#     print("No numbers provided.")
#
#
#
# ############-python function to print factorial of numbers-######
# ############################APPROACH-1###################################
#
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))
#
# ############################APPROACH-2###################################
#
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# num=int(input("enter a no:"))
# print(factorial(num))
# ############################APPROACH-2###################################
# ###----------------------using range()----------------------------------------
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# # Take input from the user
# number = int(input("Enter a number: "))
#
# # Calculate factorial
# result = factorial(number)
#
# # Print the result
# print(f"The factorial of {number} is {result}.")
#
#
# from pyspark.sql import SparkSession
#
#
# read two files and compare the count
#
import pandas as pd
def read_fun(path):
    print("i am reading data from :", path)
    a = pd.read_csv(path)
    return a
source=read_fun(r"C:\Users\bbhoi\Desktop\all_desktop_files_folders\sreeni_data_compare\source.csv")
print(source)
target=read_fun(r"C:\Users\bbhoi\Desktop\all_desktop_files_folders\sreeni_data_compare\target.csv")


def count_check(source, target):
 source_count = source.shape[0]
 target_count = target.shape[0]
 if source_count == target_count:
  print(f"count is matching: source count is {source_count} and target count is {target_count}")
 else:
  print(f"count is not matching:  source count is {source_count}, target count is {target_count} and difference "
        f"is {source_count - target_count}")


count_check(source, target)


def data_compare(source, target):
     return source.compare(target)


print("data comparision:",data_compare(source, target))



# from pyspark.sql.types import *
# from pyspark.sql import SparkSession
# from pyspark.sql.types import *
# from pyspark.sql.functions import *
# from pyspark.sql.window import Window
#
# emp_data = [
#  (1,"Joe", 85000, 1),
#  (2,"Henry", 80000, 2),
#  (3,"Sam", 60000, 2),
#  (4,"Max", 90000, 1),
#  (5,"Janet", 69000, 1),
#  (6,"Randy", 85000, 1),
#  (7,"Will", 70000, 1)
# ]
# print(emp_data)
#
#
# emp_schema = StructType([
#  StructField("id",IntegerType(),True),
#  StructField("name",StringType(),True),
#  StructField("salary",IntegerType(),True),
#  StructField("dep_id",IntegerType(),True)
# ])
#
# print(emp_schema)
#
# dep_data = [
#  (1,"IT"),
#  (2,"Sales")
# ]
#
# dep_schema = StructType([
#  StructField("id",IntegerType(),True),
#  StructField("name",StringType(),True)
# ])
#
# print(dep_schema)
# print(dep_data)
#
# emp_df = spark.createDataFrame(emp_data,emp_schema)
# emp_df.show()
#
# dep_df = spark.createDataFrame(dep_data,dep_schema)
# dep_df.show()
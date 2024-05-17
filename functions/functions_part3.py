
# Count occurrences of a character in a string:
# Find the maximum of three numbers:
# write python function to print factorial of numbers
# read two files and compare the count

############## Count occurrences of a character in a string:###########
# (((((((((((((((((((((((((((((((((APPROACH-1)))))))))))))))))))))))))))))))
# def count_occurences(string,char):
#     str_count=string.count(char)
#     print(str_count)
#     return str_count
# print(count_occurences("Babulu","l"))

# (((((((((((((((((((((((((((((((((APPROACH-2)))))))))))))))))))))))))))))))

# def count_occurences(string,char):
#     str_count=string.count(char)
#     print(str_count)
#     return str_count
# string=input("enter string:")
# char=input("enter char:")
# count_char=string.count(char)
# print(count_char)

##########################Find the maximum of three numbers:####################
##(((((((((((((((((((((((((((-APPROACH-1-)))))))))))))))))))))))))))))))))))))##
# def max_3_num(a,b,c):
#     m3=max(a,b,c)
#     return(m3)
# max_num=max_3_num(1,2,3)
# print(max_num)

############################python function to print factorial of numbers#########
##((((((((((((((((((((((((((--APPROACH-1-)))))))))))))))))))))))))))))))))))))))))

# factorial of given number
# def factorial(n):
#     # single line to find factorial
#     return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
#
#
# # Driver Code
# num = 6
# print("Factorial of", num, "is", factorial(num))

###########################APPROACH-2##################################
#
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i  # result = result * i
#     print(f"factorial of {n} is", result)
#     return result
# factorial(5)

######################python function to print prime numbers############
##(((((((((((((((((((((((--APPROACH-1--))))))))))))))))))))))))))))))))##
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
print(is_prime(17))


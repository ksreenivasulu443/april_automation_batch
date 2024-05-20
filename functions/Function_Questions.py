# Count occuarance of character in a string

# def str_count(str2):
# 
#    repeated_char= str2.count(str2)
#    result = str2.find(str2)
#    return repeated_char,result
# str=input('enter the string')
# 
# print(str_count(str))

def count_repeated_characters(input_string):
    char_count = {}
    for char in input_string:
        # Check if the character has already been counted
        if char not in char_count:
            # Count the occurrences of the character in the string
            count = input_string.count(char)
            # If the character occurs more than once, find its first index
            if count > 1:
                first_index = input_string.find(char)
                # Store the character count and its first index
                char_count[char] = (count, first_index)
    return char_count

# Test the function
input_string = "sreeni"
result = count_repeated_characters(input_string)
print("Character counts:", result)



#find max of 3 numbers
# def max_num(a,b,c):
#     if a>b and a>c:
#         print('a is max',a)
#     elif b>a and b>c:
#         print('b is max',b)
#     else:
#         print('c is max',c)
# max_num(10,20,30)
#
# def max_num1(a,b,c):
#     result1=max(a,b,c)
#     result2 = min(a, b, c)
#     return result1,result2
# print(max_num1(2,3,4)
#
# factorial
# def fact_num(a):
#     result=1
#     for i in range(1,a+1):
#         result=result*i
#     print(result)
# fact_num(0)

# recursive function
# def fact_num1(a):
#     if a==0:
#         return 1
#     else:
#         return a*fact_num1(a-1)
# print(fact_num1(5))
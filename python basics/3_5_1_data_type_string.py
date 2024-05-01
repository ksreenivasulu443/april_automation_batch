# 5. Str(): string is collection of characters, enclosed within single quotes or double quotes.
'''
* hold the Characters
* Insertion order is preserved
* Duplicate allows
* indexing applicable(Every character in the string is represented unique index, supports
forward(start with 0) and backward(start with -1) index)
* slicing applicable
* Immutable (value assignments is not possible or not able to change the value)
Methods: Index, Multiplication, Concatenate, len, count, replace, joining, splitting, case of sting(upper, lower,
swapcase, title, capitalize), start and ending part of string(startswith, endswith), formatting, comparison,
check the characters present in a string(isalnum, isalpha, isdigit, islower, isupper, istitle, isspace), slicing, strip
'''


string = 'ETL'

print('the vale of the string is', string)
print("type of the string is", type(string))
print("memory address of string is", id(string))

string1 = "ETL"
print('the vale of the string1 is', string1)
print("type of the string1 is", type(string1))
print("memory address of string1 is", id(string1))

string2 = """ETL"""
print('the vale of the string2 is', string2)
print("type of the string2 is", type(string2))
print("memory address of string2 is", id(string2))

print("methods are available in sting data type", dir(str))

string5 = 'Big Data | Testing'
print(f"count of a in {string5}", string5.count('a'))
print(f"count of a in {string5}", string5.count('a'), string5.count('|'))
print(f"string5 value stat with Auto in {string5} : ", string5.startswith('Big'))


# text = input("enter the txt value: ")
#
# print(f"count of a in {text}", text.startswith('Big'))
# print(f"count of a in {text}", text.endswith("Testing"))
# print(f"count of a in {text}", text.find("Data", 0))


# join & revers string
print("-----join &revers string------")
str0 = ''.join(reversed(string))
print(str0)

# Multiplication
print("-----Multiplication string------")
stl = string*3
print('the vale of the stl is', stl)
print("type of the stl is", type(stl))
print("memory address of strl is", id(stl))

# concatenate : concat of two or more string
# Ex:
first_name = 'Ram'
last_name = 'Kumar'

print("-----Concatenate of string------")
print(first_name + last_name)
full_name = first_name + " " + last_name
print(full_name)

# len length of the string
print("-----length of string------")
print(f"length of {full_name} is ", len(full_name))

# count : count the repeated character in string
print("-----count of character in string------")
print(f"count of a character in {full_name} is :", full_name.count("a"))
print(f"count of a & m character in {full_name}", full_name.count('a'), full_name.count('m'))

# replace
print("-----replace value of the string------")
n1 = full_name.replace("Kumar", "Shetty")
print(f"change the lastname in fullname ({full_name}) to", n1)


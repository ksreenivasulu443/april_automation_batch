# 5. Str(): string is collection of characters, enclosed within single quotes or double quotes.
'''
* hold the Characters
* Insertion order is preserved
* Duplicate allows
* indexing applicable(Every character in the string is represented unique index, supports
forward(start with 0) and backward(start with -1) index)
* slicing applicable
* Immutable (value assignments is not possible or not able to change the value)
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

string3 = 'ETL automation testing'

print('the vale of the string3 is', string3)
print("type of the string3 is", string3.capitalize())
print("memory address of string3 is", string3.title())

string4 = 'ETL automation testing'

print('the vale of the string4 is', string4)
print("type of the string4 is", string4.casefold())
print("memory address of string4 is", string4.lower())
print("memory address of string4 is", string4.swapcase())
print("memory address of string4 is", string4.upper())

x = string4.center(40)
print(x)

string5 = 'Big Data | Testing'
print(f"count of a in {string5}", string5.count('a'))
print(f"count of a in {string5}", string5.count('a'), string5.count('|'))
print(f"string5 value stat with Auto in {string5} : ", string5.startswith('Big'))


text = input("enter the txt value: ")

print(f"count of a in {text}", text.startswith('Big'))
print(f"count of a in {text}", text.endswith("Testing"))
print(f"count of a in {text}", text.find("Data", 0))


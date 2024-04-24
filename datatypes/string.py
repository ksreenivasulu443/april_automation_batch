"""This module file is create to practice python string datatypes
created by Sreeni on 04/23/2024
"""

string = 'ETL'

print("The value of string is ", string)
print("type of string is ", type(string))
print("Memory of string", id(string))

string2 = "ETL"

print("The value of string2 is ", string2)
print("type of string2 is ", type(string2))
print("Memory of string2", id(string2))

string3 = """ETL"""

print("The value of string3 is ", string3)
print("type of string3 is ", type(string3))
print("Memory of string3", id(string3))

string4 = '''ETL'''

print("The value of string4 is ", string4)
print("type of string4 is ", type(string4))
print("Memory of string4", id(string4))

string = " I don't care "

print("The value of string is ", string)
print("type of string is ", type(string))
print("Memory of string", id(string))

string = ' I don"t care '

print("The value of string is ", string)
print("type of string is ", type(string))
print("Memory of string", id(string))

string = """i don't care """
string = '''i don"t care '''
etl_string= '''ETL in testing means an extract, transform and load process that reads data from multiple source systems,
 transports it to a data transformation layer for further processing which includes cleaning,
consolidating, integrating, and then loading into a target database or file'''

print("The value of etl_string is ", etl_string)
print("type of etl_string is ", type(etl_string))
print("Memory of etl_string", id(etl_string))

print(dir(etl_string))

print("methods available in string datatype",dir(etl_string))

str7 = 'ETL AUTOMATION'
print("Before capitalize str7 is ", str7)
print("After capitalize str7 is", str7.capitalize())

print("Before casefold str7 is ", str7)
print("After casefold str7 is", str7.casefold())

print("Before lower str7 is ", str7)
print("After lower str7 is", str7.lower())

txt = "banana"
x = txt.center(10)
print(x)
str8 = 'BIG DATA TESTING'
print(f"count of e in {str8}", str8.count('a'))

print("*"*50)

str = "Automation Testing"

print("str.startswith('Auto')",str.startswith('Auto'))
print("str.startswith('auto')",str.startswith('auto'))
print("Ends with Testing ",str.endswith('Testing'))
print("str.endswith('testing')",str.endswith('testing'))

print("str.find('Test')",str.find('Test'))

print("str.find('i')",str.find('i'))

print("str.find('i',8)",str.find('i',8))

print("str.find('i',8,12)",str.find('i',8,12))

name = 'Hari'
age = 24

print("My name is {name} and age is {age}".format(name=name,age= age))
name = 'Sreeni'
age = 25
print(f"My name is {name} and age is {age}")

env = ['dev', 'qa']
table = ['emp', 'dept']
for i in env:
    for j in table:
    #print(i)
        print(f"select * from {i}.{j}")

str = 'ETLbatch3'

print(f"str.isalnum() on {str}", str.isalnum())
str2 = 'ETL_batch3'
print(f"str2.isalnum() on {str2}", str2.isalnum())

str3 = 'ETLbatch'
print(f"str3.isalnum() on {str3}", str3.isalpha())

str4 = 'ETLbatch1'
print(f"str4.isalnum() on {str4}", str4.isalpha())

str = ' Sreeni Kattu  '
print("length of str before strip", len(str))
print(f"str.strip()", str.strip())
print("length of str after strip", len(str.strip()))

print(f"str.rstrip()", str.lstrip())
print("length of str after lstrip", len(str.lstrip()))
print(f"str.lstrip()", str.lstrip())
print("length of str after rstrip", len(str.rstrip()))
str7 = 'ETL Automation'
print(f"str7.lstrip()", str7.rstrip('Automation'))
str8 = 'ETL Automation'
print(f"str8.lstrip()", str8.lstrip('ETL'))

str9 = 'ETL-Bigdata-testing-automation'
str10 = 'ETL,Bigdata,testing,automation'

print('str9.split("-",2)',str9.split("-"))
print('str10.split(",",2)',str10.split(","))
print('type str10.split(",",2)',type(str10.split(",")))
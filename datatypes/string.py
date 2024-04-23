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
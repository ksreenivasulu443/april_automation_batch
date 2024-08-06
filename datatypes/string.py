# """This module file is create to practice python string datatypes
# created by Sreeni on 04/23/2024
# """
#
# string = 'ETL'
#
# print("The value of string is ", string)
# print("type of string is ", type(string))
# print("Memory of string", id(string))
#
# string2 = "ETL"
#
# print("The value of string2 is ", string2)
# print("type of string2 is ", type(string2))
# print("Memory of string2", id(string2))
#
# string3 = """ETL"""
#
# print("The value of string3 is ", string3)
# print("type of string3 is ", type(string3))
# print("Memory of string3", id(string3))
#
# string4 = '''ETL'''
#
# print("The value of string4 is ", string4)
# print("type of string4 is ", type(string4))
# print("Memory of string4", id(string4))
#
# string = " I don't care "
#
# print("The value of string is ", string)
# print("type of string is ", type(string))
# print("Memory of string", id(string))
#
# string = ' I don"t care '
#
# print("The value of string is ", string)
# print("type of string is ", type(string))
# print("Memory of string", id(string))
#
# string = """i don't care """
# string = '''i don"t care '''
# etl_string= '''ETL in testing means an extract, transform and load process that reads data from multiple
#                source systems, transports it to a data transformation layer for further processing which
#                includes cleaning,consolidating, integrating, and then loading into a target database or file'''
#
# print("The value of etl_string is ", etl_string)
# print("type of etl_string is ", type(etl_string))
# print("Memory of etl_string", id(etl_string))
#
#
#
# print("methods available in string datatype",dir(etl_string))
#
# str7 = 'ETL Automation testing'
# print("Before capitalize str7 is ", str7)
# print("After capitalize str7 is", str7.capitalize())
# print("After title str7 is", str7.title())
# #
#
# print("Before casefold str7 is ", str7)
# print("After casefold str7 is", str7.casefold())
# print("After lower str7 is", str7.lower())
# print("After swapcase str7 is", str7.swapcase())
# print("After upper str7 is", str7.upper())
#
#
# txt = "ETL Testing"
# x = txt.center(100)
# print(x)
#
# str8 = 'BIG DATA TESTING 1| 4342 [472534623542 '
# print(f"count of A in {str8}", str8.count('A'))
# print(f"count of | in {str8}", str8.count('|',20,30))
#
# name = 'Sreeni'
# print(f"count of en in {name} and n ", name.count('en'),name.count('n'))
#
#
#
#
#
# print("*"*50)
#
# str = input("enter str value:") # input, raw_input
#
# print(f"str.startswith('Auto') in {str} : ",str.startswith('Auto'))
#
# print(f"str.startswith('Auto') in {str} : ",str.startswith('auto'))
#
# print("Ends with Testing ",str.endswith('Testing'))
#
# print(help(str.startswith))
# print(help(str.endswith))
#
# str ='TESTING'
# print("str.find('Test')",str.find(' Test'))
# print("str.find('i')",str.find('i'))
# #
# print("str.find('i',8)",str.find('i',8))
#
# print("str.find('i',8,12)",str.find('i',8,12))
#
# name = 'Prashant'
# age = 24
# sname = 'K'
# #
# print(f"name is {name} and age is {age}")
# print("name is {first_name} and age is {person_age}".format(person_age= age,first_name=name))
# print("firstname is {} and lastname is {} and age {} ".format(name,sname,age))
#
#
# schema = input("enter schema:")
# table = input("enter table name:")
# second_table = input("enter second table:")
# key_column = input("enter key column table:")
# age = input("enter age :")
#
# query = f"""select count(1) from {schema}.{table} a inner join {schema}.{second_table} b
#          on a.{key_column}=b.{key_column} where age<{age} """
# env=['test']
# print(query)
# for i in env:
#     for j in table:
#         #print(f"select * from {i}.{j}")
#         print("select * from {}.{}".format(i,j))
#
# str = 'ETLbatch5'
#
# print(f"str.isalnum() on {str}", str.isalnum())
#
#
# str2 = 'ETL batch 3'
# print(f"str2.isalnum() on {str2}", str2.isalnum())
#
# str3 = 'ETLbatch'
# print(f"str3.isalnum() on {str3}", str3.isalpha())
#
# str4 = 'ETLbatch1'
# print(f"str4.isalnum() on {str4}", str4.isalpha())
#
# str = ' Sreeni Kattu  '
# print("length of str before strip", len(str))
# print(f"str.strip()", str.strip())
# print("length of str after strip", len(str.strip()))
# #
# print(f"str.rstrip()", str.lstrip())
# print("length of str after lstrip", len(str.lstrip()))
# print(f"str.lstrip()", str.lstrip())
# print("length of str after rstrip", len(str.rstrip()))
#
# str = '#Sre#eni#'
# print("str.strip('#')",str.strip("#"))
# str7 = 'ETL Automation'
# print(f"str7.lstrip()", str7.rstrip('Automation'))
# str8 = 'ETL Automation'
# print(f"str8.lstrip()", str8.lstrip('ETL'))
#
# str9 = 'ETL-Bigdata-testing-automation'
# str10 = 'ETL,Bigdata,testing,automation'
#
# print('str9.split("-",2)',str9.split("-"))
# print('str10.split(",",2)',str10.split(","))
# print('type str10.split(",",2)',type(str10.split(",")))
#
# a = "MyFolder"
# b = "Demo002"
# c = "2bring"
# d = "my demo"
#
# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())
#
# txt = "Company123RRږ"
#
# x = txt.isascii()
#
# print(x)
# #
# myTuple = ["John", "Peter", "Vicky"]
#
#
# x = ",".join('sreeni','K')
#
# print(x)
#
# key_column = ['c1','c2','c3']
# key_cols = ",".join(key_column)
# #
# # query = f" select {key_cols}, count(1) from table group by {key_cols} having count(1)"
# #
# # print(query)

# a = "i don't care"
# print(a)
#
# string = 'ETL'
# print('the value of string is :', string)
# print('the type of string is :', type(string))
# print('the memory address of string is :', id(string))
#
# string_0 = '''ETL'''
# print('the value of string_0 is :', string_0)
# print('the type of string_0 is :', type(string_0))
# print('the memory string_0 of string is :', id(string_0))
#
# string_1 = "ETL"
# print('the value of string_1 is :', string_1)
# print('the type of string_1 is :', type(string_1))
# print('the memory address of string_1 is :', id(string_1))
#
# string_2 = """ETL"""
# print('the value of string_2 is :', string_2)
# print('the type of string_2 is :', type(string_2))
# print('the memory address of string_2 is :', id(string_2))
#
# string_2 = "i don't care"
# print(string_2)
#
# string_02 = """i don't care"""
# print(string_02)
#
# string_3 = 'i don"t care'
# print(string_3)
#
# string_03 = '''i don"t care'''
# print(string_03)
#
# etl = """ETL in testing means an extract, transform and load" process that reads data
#          from multiple source systems, transports, it to a data transformation layer
#          for further" processing which includes'' cleaning, consolidating, integrating,
#          and then loading into a target database or file"""
# print('the value of etl is :', etl)
# print('the type of etl is :', type(etl))
# print('the memory address of etl is :', id(etl))

# etl_1 = 'Prashant'
# print("methods available in string datatype",dir(etl_1))

""""['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 
     'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 
     'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
     'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 
     'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
     'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']"""

# print("*"*200)
#
# # capitalize
# str = 'ETL Automation'
# print("Before capitalize the str is:",str)
# print("after capitalize the str is:",str.capitalize())
#
# # upper
# str01 = 'ETL Automation'
# print("Before upper the str01 is:",str01)
# print("after upper the str01 is:",str01.upper())
#
#
# # casefold
# str1 = 'ETL Automation'
# print("Before casefold the str1 is:",str1)
# print("after casefold the str1 is:",str1.casefold())
# print("after lower the str3 is:",str1.lower())
#
# # center
# str2 = 'ETL Automation'
# str02 = str2.center(50)
# print("Before center the str2 is:",str02)
#
# # lower
# str3 = 'ETL Automation'
# print("Before lower the str3 is:",str3)
# print("after lower the str3 is:",str3.lower())
#
# # title
# str4 = 'ETL Automation'
# print("Before title the str4 is:",str4)
# print("after title  the str4 is:",str4.title())
#
# # swapcase
# str5 = 'ETL Automation'
# print("Before swapcase the str5 is:",str5)
# print("after swapcase  the str5 is:",str5.swapcase())
#
# str6 = "banana"
# print("the count of a in the given str6 is :",str6.count('a'))
#
# str7 = "banana@gamil.com"
# print("the count of @ in the given str7 is :",str6.count('@'))
#
# str8 = "banana@gamil********.com"
# print("the count of * in the given str8 is :",str8.count('*'))
#
# name = 'sreeni'
# print(f"the count of 's' is {name} :",name.count('s',1,0))
#
# name = 'sreeni'
# print(f"the count of 's' is {name} :",name.count('s',1,1))
#
# name = 'sreeni'
# print(f"the count of 's' is {name} :",name.count('s',1,2))
#
# name = 'sreeni'
# print(f"the count of 'e' is {name} :",name.count('e',2,5))
#
# name = 'sreeni'
# print(f"the count of 'ree' is {name} :",name.count('ree'))
#
# name = 'sreeni'
# print(f"the count of 'sre' is {name} and eni :",name.count('sre'),name.count('eni'))
#
# name = 'sreeni'
# print(f"the count of 'sre' is {name} and eni :",name.count('sre'),name.count('eni'),name.upper(),name.lower())

# str = 'Automation Testing'
# print(f"str.startswith('Auto') in {str} is :", str.startswith('Auto'))
# print(f"str.endswith('Auto') in {str} is :", str.endswith('Testing'))
#
# str = input('Automation Testing :')
# print(f"str.startswith('Auto') in {str} is :", str.startswith('Auto'))
# print(f"str.startswith('Auto') in {str} is :", str.startswith('Auto'))
#
# print(help(str.startswith))
# print(help(str.endswith))

# find

# str ='TESTING'
# # print("str.find('Test')",str.find(' Test'))
# # print("str.find('i')",str.find('i'))
# print("str.find('Test')",str.find('TESTING'))
# print("str.find('I')",str.find('I'))
#
# str1 = "ETL Automation"
# print("str1.find('i')",str1.find('i'))
# print("str1.find('L')",str1.find('L'))
#
# name = 'Prashant'
# age = 24
# sname = 'K'
# #
# print(f"name is {name} and age is {age}")
# print("name is {first_name} and age is {person_age}".format(person_age= age,first_name=name))
# print("firstname is {} and lastname is {} and age {} ".format(name,sname,age))

print("*"*50)

# schema = input("enter schema:")
# table = input("enter table name:")
# second_table = input("enter second table:")
# key_column = input("enter key column table:")
# age = input("enter age :")
#
# query = f"""select count(1) from {schema}.{table} a inner join {schema}.{second_table} b
#          on a.{key_column}=b.{key_column} where age<{age} """
# env=['test']
# print(query)
# for i in env:
#     for j in table:
#         #print(f"select * from {i}.{j}")
#         print("select * from {}.{}".format(i,j))

# isalnum
str = 'ETL batch 3'
print(f"legnth of {str} : ", len(str))
print(f"str.isalnum is {str}:",str.isalnum())

str1 = 'ETLbatch3'
print(f"str1.isalnum is {str1}:",str1.isalnum())




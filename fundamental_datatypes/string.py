# -------------------STRING-------------------

# str="data engineering"
# print(str)
# print(type(str))
# print(id(str))
# print(dir(str))

# str='elt testing'
# print(str.capitalize())

# str1='etl testing'
# str2='ETL TESTING'
# if str1.casefold()==str2.casefold():
#     print("str1=str2")
# else:
#     print("str1<>str2")


# str='etl testing'
# print(str.upper())

# str="ETL TESTING"
# print(str.lower())

# str='etl testing'
# print(str.swapcase())

# str='ETL TESTING'
# print(str.swapcase())

# str='Etl Testing'
# print(str.swapcase())

# str='ETL TESTING'
# print(str.center(100))

# str='ETL TESTING'
# print(str.count('T'))
# print(f"count of T in {str} is:",str.count('T'))
# print(f"count of | in {str} is:",str.count('|'))
# print(f"count of TEST in {str}",str.count('TEST'),"and count of TL in {str}",str.count("TL"))

# print("*"*150)

# str=input("enter value:")
# print(f"str.startswith('Auto') in {str}",str.startswith('Auto'))
# print(f"str.endswith('Test') in {str}",str.endswith('ing'))

# print(help(str.startswith))
# print(help(str.endswith))
#
# str='etl testing automation'
# print("str.find('TEST'):",str.find('TEST'))
#
# str='etl testing automation'
# print("str.find('ing'):",str.find('ing'))

# name='Babulu'
# age=30
# surname='Bhoi'

# print("my name is {}, age is {} and surname is {}".format(name,age,surname))
# print(f"my name is {name}, age is {age} and surname is {surname}")

#
# schema=input('enter schema:')
# table1=input('enter table1:')
# table2=input('enter table2:')
# key_column=input('enter key_column:')
# key_column_value=input('enter key_column_value:')
# emp_sal_lt_1000=f"""select count(*) from {schema}.{table1} a inner join {schema}.{table2} b
# on a.{key_column}=b.{key_column}
# where key_column_value<{key_column_value}"""
# print(emp_sal_lt_1000)

# ################isalnum()alphanumeric -True, non-alphanumeric-False########

# str='ETL AUTOMATION'
# print(str.isalnum())
#
# str='ETLAUTOMATION123'
# print(str.isalnum())

# ########################isalpha()---only alphabates-True, else-False

# str='ETLAUTOMATION'
# print(str.isalpha())

# print("concatenate str1 & str2:",str1+str2)
# print("multiply str1 & 2:",str1*2)
#
# ###########strip-- removes leading & trailing white spaces, tabs, newlines

# str=('12345automation of etl'
#      'testing')
# print(str.strip('12345'))
#

# str='     babulu bhoi     '
# print("length before strip:",len(str))
# print("length after strip:",len(str.strip()))
#
# print(len(str.lstrip()))
# print(len(str.rstrip()))

# str1='etl-bigdata-testing'
# str2='etl,bigdata,testing'
# str3='etl bigdata testing'
# str4='etl bigdata automation testing'
#
# print(str1.split())
# print(str2.split())
# print(str3.split())
# print(str4.split(maxsplit=2))

# date='02-08-2021'
# print(date.split('-'))
# print(date.split('-',maxsplit=1))

# dd='11-22-33-44-55'
# print(dd.split('-',maxsplit=3))

# string1 = "variable_name"
# string2 = "123_variable"
# string3 = "_variable"
# string4 = "class"
#
# print(string1.isidentifier())  # Output: True
# print(string2.isidentifier())  # Output: False (starts with a digit)
# print(string3.isidentifier())  # Output: True
# print(string4.isidentifier())  # Output: True

string1 = "Hello"
string2 = "Привет"
string3 = "Hello123"
string4 = "😊"

print(string1.isascii())  # Output: True
print(string2.isascii())  # Output: False (contains non-ASCII characters)
print(string3.isascii())  # Output: True
print(string4.isascii())  # Output: False (contains non-ASCII characters)
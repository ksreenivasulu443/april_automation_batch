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



print("methods available in string datatype",dir(etl_string))

str7 = 'ETL Automation testing'
print("Before capitalize str7 is ", str7)
print("After capitalize str7 is", str7.capitalize())
print("After title str7 is", str7.title())
#

print("Before casefold str7 is ", str7)
print("After casefold str7 is", str7.casefold())
print("After lower str7 is", str7.lower())
print("After swapcase str7 is", str7.swapcase())
print("After upper str7 is", str7.upper())


txt = "ETL Testing"
x = txt.center(100)
print(x)

str8 = 'BIG DATA TESTING 1| 4342 [472534623542 '
print(f"count of A in {str8}", str8.count('A'))
print(f"count of | in {str8}", str8.count('|',20,30))

name = 'Sreeni'
print(f"count of en in {name} and n ", name.count('en'),name.count('n'))





print("*"*50)

str = input("enter str value:") # input, raw_input

print(f"str.startswith('Auto') in {str} : ",str.startswith('Auto'))

print(f"str.startswith('Auto') in {str} : ",str.startswith('auto'))

print("Ends with Testing ",str.endswith('Testing'))

print(help(str.startswith))
print(help(str.endswith))

str ='TESTING'
print("str.find('Test')",str.find(' Test'))
print("str.find('i')",str.find('i'))
#
print("str.find('i',8)",str.find('i',8))

print("str.find('i',8,12)",str.find('i',8,12))

name = 'Prashant'
age = 24
sname = 'K'
#
print(f"name is {name} and age is {age}")
print("name is {first_name} and age is {person_age}".format(person_age= age,first_name=name))
print("firstname is {} and lastname is {} and age {} ".format(name,sname,age))


schema = input("enter schema:")
table = input("enter table name:")
second_table = input("enter second table:")
key_column = input("enter key column table:")
age = input("enter age :")

query = f"""select count(1) from {schema}.{table} a inner join {schema}.{second_table} b
         on a.{key_column}=b.{key_column} where age<{age} """
env=['test']
print(query)
for i in env:
    for j in table:
        #print(f"select * from {i}.{j}")
        print("select * from {}.{}".format(i,j))

str = 'ETLbatch5'

print(f"str.isalnum() on {str}", str.isalnum())


str2 = 'ETL batch 3'
print(f"str2.isalnum() on {str2}", str2.isalnum())

str3 = 'ETLbatch'
print(f"str3.isalnum() on {str3}", str3.isalpha())

str4 = 'ETLbatch1'
print(f"str4.isalnum() on {str4}", str4.isalpha())

str = ' Sreeni Kattu  '
print("length of str before strip", len(str))
print(f"str.strip()", str.strip())
print("length of str after strip", len(str.strip()))
#
print(f"str.rstrip()", str.lstrip())
print("length of str after lstrip", len(str.lstrip()))
print(f"str.lstrip()", str.lstrip())
print("length of str after rstrip", len(str.rstrip()))

str = '#Sre#eni#'
print("str.strip('#')",str.strip("#"))
str7 = 'ETL Automation'
print(f"str7.lstrip()", str7.rstrip('Automation'))
str8 = 'ETL Automation'
print(f"str8.lstrip()", str8.lstrip('ETL'))

str9 = 'ETL-Bigdata-testing-automation'
str10 = 'ETL,Bigdata,testing,automation'

print('str9.split("-",2)',str9.split("-"))
print('str10.split(",",2)',str10.split(","))
print('type str10.split(",",2)',type(str10.split(",")))

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

txt = "Company123RRږ"

x = txt.isascii()

print(x)
#
myTuple = ["John", "Peter", "Vicky"]


x = ",".join('sreeni','K')

print(x)

key_column = ['c1','c2','c3']
key_cols = ",".join(key_column)
#
# query = f" select {key_cols}, count(1) from table group by {key_cols} having count(1)"
#
# print(query)
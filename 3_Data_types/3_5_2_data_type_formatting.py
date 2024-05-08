name = "Ajay"
Age = 29

print(f"name is {name} and ange is {Age}")
print("name is {name} and ange is {Age}".format(name=name, Age=Age))


env =['DEV', 'QA', 'PROD', 'PerPROD']
table = ['EMP', 'DEPT']

for i in env:
    for j in table:
        # print(f"select * from {i}.{j}")
        print("select * from {}.{}".format(i, j))

# schema = input("enter schema: ")
# table1 = input("enter table name: ")
# table2 = input("enter table name: ")
# key_column = input("enter column name: ")
# query = (f"""select * from {schema}.{table1} a inner join {schema}.{table2} b
# on a.{key_column}=b.{key_column} where age>18""")

# print(query)

# String Packing or joining
print("-----String Packing or joining------")
myTuple = ("c1","c2", "c3")
x = ", ".join(myTuple)
print(x)

key_clm = ("c1,c2,c3")
query1 = (f"select {key_clm} from table group by {key_clm} having count(*)>1")
print(query1)

# String Splitting
print("-----String Splitting------")
name4 = " Ram Sita "
print(f"split the wards of {name4} is:", name4.split())

# String strip
print("-----String Splitting------")
print(f"Remove the unwanted space in {name4} is", len(name4.strip()))


# case of sting(upper, lower,  swapcase, title, capitalize)
print("-----case of sting------")
string3 = 'ETL automation testing'

print(f"Capitalize - In {string3} only 1st character convert to upper case:", string3.capitalize())
print(f"Upper - In {string3} All character convert to upper case:", string3.upper())
print(f"Lower - In {string3} All character convert to Lower case:", string3.lower())
print(f'''swapcase - In {string3} All upper case character convert to Lower case and All Lower case character "
      convert to Lower case:''', string3.swapcase())
print(f"Title - In {string3} 1st character in every word convert to Upper case:", string3.title())
print("type of the string4 is", string3.casefold())

x = string3.center(40)
print(x)

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

schema = input("enter schema: ")
table1 = input("enter table name: ")
table2 = input("enter table name: ")
key_column = input("enter column name: ")
query = (f"""select * from {schema}.{table1} a inner join {schema}.{table2} b
on a.{key_column}=b.{key_column} where age>18""")

print(query)


myTuple = ("c1","c2", "c3")
x = ", ".join(myTuple)
print(x)

key_clm = ("c1,c2,c3")
query1 = (f"select {key_clm} from table group by {key_clm} having count(*)>1")
print(query1)


name4 = " Ram Sita "
print("length of the name4 before strip", len(name4))
print("strip function", len(name4.strip()))

name5 = " Ram Sita "
print("length of the name4 before strip", len(name4))
print("strip function", len(name4.strip()))



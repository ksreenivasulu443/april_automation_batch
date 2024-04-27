
str1 = 'sandy is the brand'
print("Before capitalise string is", str1)
print("After capitalise string is", str1.capitalize())
print("After title str1 is", str1.title())

print("After casefold str is", str1.casefold())
print("After casefold str is", str1.lower())

print("After swapacse str is", str1.swapcase())
print("After upper str is", str1.upper())


txt = "sandy is the king"
x=txt.center(100)
print(x)

var = "You can do this"
print(f"count of o in {var}",var.count('dp'))


#str2 = input("Enter str value:")
#print(f"str.startswith input value in {str2}: ",str2.startswith('team'))


schema = input("Enter Schema name")
table = input("Enter Table name")
secondtable = input("Enter secondtable:")
keycolumn = input("Enter Key column name")

query = f""""select * from {schema}.{table} a inner join {schema}.{secondtable} b
        on a.{keycolumn}=b.{keycolumn} """

print(query)

Print













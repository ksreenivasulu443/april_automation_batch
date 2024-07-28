string:'ETL'
string1:"""etl"""
sting2:""etl""
sting3:'''etl'''
string:"i don't care"



print("the  value of string",string)
print("type of string,type(string)
print("memory of the sting is",id(string)

str='ETL'

print("after lower str is",str.lower())
print("after casefold str is",str.casefold())
print("after upper str is",str.upper())
print("after swapcase str is",str.swapcase())

txt="ETL"
x=txt.center(100)
print(x)

str="aabbcc122//"

print(f"count of a in {str}",str.count('a'))

name = 'shamim'
print(f"count of m in {name}",name.count('m'))

different argument print statement:
print(f"count of m in {name}",name.count('m'),name.count('a'))

str='testing'

print("str.find('ng')",str.find('ng'))

name='shamim'
age=30
print(f"name is {name},age is  {age}") -----here name is one argument and age is another argument

real time exp for format(f) in string :
env=['QA','dev']
table=['emp','dept']

for i in env
for j in table
print (f"select * from {i}.{j}")

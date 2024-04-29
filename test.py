str ='ETL AUTOMATION'

str = 'seenu.k8@gmail.com'
print(str[0:str.find('A')])

print(str[0:str.find('@')])

print(str[str.find('@')+1:str.rfind('.')])
print(str[str.rfind('.')+1:])

print(str[0])

print(str[1])

txt = "I could eat bananas all day"

x = txt.partition("eat")

print(x)

txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

txt = "50"

x = txt.zfill(10)

print(x)

print("str[1:10:-1]",str[1:10:-1])




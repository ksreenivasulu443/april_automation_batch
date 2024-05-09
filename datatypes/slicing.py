
str='ETL'
print('str value is',str)
#syntax str[start:end:step]
print(f'1st character of {str}',str[0])
print(f'1st character of {str}',str[1])
print(f'1st character of {str}',str[2])
print(f'1st character {str[0]},2nd character{str[1]},3rd character{str[2]}')

str2='ETL AUTOMATION'
print(f'fetch the group of characters {str2}',str2[0:4]) # end=end-1

#print(f'fetech 4 the character{str}',str[4])
print(f'fetech 4 the character{str2}',str2[0:])
print(f'fetech 4 the character{str2}',str2[4:])
print(f'fetech 4 the character{str2}',str2[:])
print(f'fetech 4 the character{str2}',str2[:5])

email='sreenu@gmail.com'
print(f'fetech the user{email}',email[0:email.find('@')])

print('fetch A',str2.find('A'))
print('fetch A',str2.rfind('A'))

print(f'fetch  the character{str2}',str2[::2])


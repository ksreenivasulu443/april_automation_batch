str = 'Welcome to Python Program'

print("str value is: ", str)

print(f"String first charter {str} is:", str[0])

print(f"String Second charter {str} is:", str[1])

print(f"String 6th charter {str} is:", str[5])

print(f"String 6th charter {str} is:", str[6-1])


emails = 'Anand.Devisetty@gmail.com'

print(f'First Name of {emails}:',emails[0:emails.find('.')])
print(f'Secondary Name of {emails}:',emails[emails.find('.')+1:emails.find('@')])
print(f'Domain name of {emails}:', emails[emails.find('@')+1:emails.rfind('.')])
print(emails[emails.rfind('.')+1:])

emails = 'Bala.Anand.Devisetty@gmail.com'
print("emails @",emails[:emails.find('@')].split('.'))
#print(f'Domain name of {emails}:', emails[emails.find('@')+1:emails.rfind('.')])
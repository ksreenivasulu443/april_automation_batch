# Ex:
first_name = 'Ram'
last_name = 'Kumar'
print("string")
print(type(first_name))
print(first_name)

# first_name[2] = 'n'
# print(first_name)

# slicing of string : slice mean a piece
# [] operator is called slice operator, R=0, a=1, m=2, / m=-1, a=-2, R=-3
# print("Index, Slice")
# print(first_name[0])
# print(first_name[0:2])
# print(first_name[-2:])

# concatenate
print("Concatenate")
print(first_name + last_name)
full_name = first_name + " " + last_name
print(full_name)

string = 'ETL'
print('the vale of the string is', string)

string1 = 'ETL_Automation_Testing'
print(f'1st character of {string1} is', string1[0])
print(f"in {string1} 1st character is {string1[0]}, 2st character is {string1[1]}, and 3rd character is {string1[2]}")
print(f'Last character of {string1} is', string1[-1])
print(f'Last character of {string1} is', string1[-12:-1])
# print(f"print 1 to 5th string from {string1} is", string1[2:5])
# print(string1[1:15:2])
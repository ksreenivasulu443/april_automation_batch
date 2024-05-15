'''
String index: fetch the specific character by using index number
slicing : fetch the range of character by using slicing(:)
[0:n] n-1
'''

string = 'ETL'
print('the vale of the string is', string)

# index ex
string1 = 'ETL_Automation_Testing'
print(f'Forward 1st index character of {string1} is', string1[0])
print(f"in {string1} 1st character is {string1[0]}, 2st character is {string1[1]}, and 3rd character is {string1[2]}")
print(f'Backward last index character of {string1} is', string1[-1])


# Slicing ex:
print("-------Slicing--------")
print(f'Forward Slicing characters of {string1} is', string1[0:5])
print(f'Backward Slicing characters of {string1} is', string1[-12:-1])
print(f"print 1 to 5th string from {string1} is", string1[2:5])

# skip character [start index no:end index no:skip no of character]
print(string1[1:15:2])

# revers string by slicing
print(string1[::-1])


# Length len
n = len(string1)
i = 0
print("Forward direction")
while i<n:
    print(string1[i], end='')
    i+= 1

i = -1
print("Backward direction")
while i>-n:
    print(string1[i], end='')
    i=i-1

print("Forward direction1")
for i in string1:
    print(i, end='')

print("Backward direction1")
for i in string1[::-1]:
    print(i, end='')

# start and ending part of string(startswith, endswith)
print("-----start and ending part of string------")
text = "Big Data Testing"
print(f"Stating ward of {text} value is:", text.startswith('Big'))
print(f"Ending ward of {text} value is:", text.endswith("Testing"))
print(f"Find the word in {text} value is:", text.find("Data", 0))
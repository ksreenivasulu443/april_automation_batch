"""This module file is create to practice python string slicing part2
created by Sreeni on 04/30/2024
"""

str = 'ETL'

print("str value is ", str)

print(f"last available in {str} is : ", str[-1])
print(f"last second character available in {str}  : ", str[-2])
print(f" last third character available in {str}  : ", str[-3])
#print(f" last fourth character available in {str}  : ", str[-4])

print(f"first cha available in {str} is : ", str[0])
print(f" second character available in {str}  : ", str[1])
print(f"  third character available in {str}  : ", str[2])
#print(f"  third character available in {str}  : ", str[3])

str = 'ETL AUTOMATION'
#A negative step value moves the slicing from right to left.
#A positive step value moves the slicing from left to right

# if step value +1 then end= end-1
# # if step value -1 then end= end+1

print("str[-12:-7:1]",str[-12:-7:1])
print("str[-12:-14:-1]", str[-12:-14:-1])

print("str[-12:-14]", str[-12:-14])

print("str[-12:-7:1]",str[-12:-7:1])

print("str[-12:-7:1]",str[-12:100:1])

print("str[0:50:1]",str[0:50:1])

print("str[100]",str[100])

print("str[-12:-2:2]",str[-12:-2:2])







print("str[3:-2:1]",str[3:-2:1])


# print("str[2:-3:2]",str[2:-3:2])
# print("str[1:-5:-1]",str[1:-5:-1])
# print("str[5:-1:-1]",str[5:-1:-1])
#
print("str[-1:5:-1]",str[-1:5:-1])
# print("str[10:5:-1]",str[10:5:-1])
#
print("str[::]",str[::])

print("str[::]",str[::-1])

str = "I don't care 5454 "
#
# print("str[-12:-7:-1]",str[-7:-12:-1])

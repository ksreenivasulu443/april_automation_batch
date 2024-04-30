"""This module file is create to practice python slicing negative_index and
    created by Prashant on 30/04/2024"""

#slicing negative_index
print("slicing_negative_index")
print("="*50)
str = 'ETL'
print(str)
print(f"the available character in {str} is :",str)
print(f"the last value of given character {str} is :", str[-1])
print(f"the second_last value of given character {str} is :", str[-2])
print(f"the thir_value of given character {str} is :", str[-3])

print(f"the last value of given character {str} is :", str[0])
print(f"the second_last value of given character {str} is :", str[1])
print(f"the thir_value of given character {str} is :", str[2])
#print(f"the fetch the given character from {str} is :", str[3])  #string index out of range



print(f"the middle character of the given {str} is :", str[-2])
#print(f"the fetch character of the given {str} is :", str[-4])  #string index out of range

str = 'ETL AUTOMATION'
# negative slicing values move from right to left
# positive slicing values move from left to right

print(str)
#str[-12:-7:1]
print("[-12:-7:1] the str[-12:-7:1] is :",str[-12:-7:1])

print("[-12:-7:1] the str[-12:-7:1] is :",str[-12:-7:-1])
print("[-14:-10:-2] the str[-14:-10:-2] is :",str[-14:-10:-2])
print("[-14:-10:-2] the str[-14:-10:-2] is :",str[-14:-10:-2])
print("[-12:-13:-1] the str[-12:-13:-1] is :",str[-12:-13:-1])
print("[-12:-14:-1] the str[-12:-14:-1] is :",str[-12:-14:-1])
print("[-12:-17:-1] the str[-12:-7:-1] is :",str[-12:-7:-1])
print("[-12:-17:1] the str[-12:-7:1] is :",str[-12:-7:1])
print("[-12:-2:2] the str[-12:-2:2] is :",str[-12:-2:2])
print("[3:-2:1] the str[3:-2:1] is :",str[3:-2:1])
print("[::1] the str[::1] is :",str[::1])
print("[3:-2:-1] the str[3:-2:-1] is :",str[-1:5:-1])
print("[::] the str[::] is :",str[::])
print("[::-1] the str[::-1] is :",str[::-1])

name = 'SIMPLIELEARN'
print(name)
print(name[-5:-2])
print(name[0:10])
print(name[0:-2:1])
print("name[0:1:1] the name[0:1:1] is :",name[0:1:1])
print("name[2:-1:1] the name[2:-1:1] is :",name[2:-1:1])
print("name[-1:-1:-1] the name[-1:-1:-1] is :",name[-1:-1:-1]) #get the update from trainee
print("name[1:1:1] the name[1:1:1] is :",name[1:1:1]) #get the update from trainee
















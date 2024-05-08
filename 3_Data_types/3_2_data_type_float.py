# 2. Float(): data type to represent floating point values, the number with decimal points
'''
* hold the decimal values
* indexing not applicable
* slicing not applicable
* Immutable (value assignments is not possible or not able to change the value)
'''


count = 10.25678904389464535767823

print('the vale of the count1 is', count)
print("type of the count1 is", type(count))
print("memory address of count1 is", id(count))

count2 = -10.25678904389464535767823

print('the vale of the count2 is', count2)
print("type of the count2 is", type(count2))
print("memory address of count2 is", id(count2))

count3 = 13621543761573578153615263162327854265451265.24567

print('the vale of the count3 is', count3)
print("type of the count3 is", type(count3))
print("memory address of count3 is", id(count3))



count4 = 5647112.798

print('the functions of the float type, count4 is', dir(count4))
print('the vale of the count3 is', count4.__float__)
print("type of the count4 is", type(count4))
print("memory address of count4 is", id(count4))
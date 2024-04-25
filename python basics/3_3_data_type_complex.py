# 3. Complex(): data type to represent complex values, in the (a+bj) a= Real part, b = Imaginary part
# In the real part we can use only int values like Whole number, Decimal, Octal, Binary, Hexa decimal
# In the Imaginary part should accept only Decimal and Whole number
'''
* hold the complex values
* indexing not applicable
* slicing not applicable
* Immutable (value assignments is not possible or not able to change the value)
'''

count = -5+32j

print('the vale of the count1 is', count)
print("type of the count1 is", type(count))
print("memory address of count1 is", id(count))



count4 = 0.1+1j

print('the methods are available in count4 is', dir(count4))
print('the vale of the count3 is', count4)
print("type of the count4 is", type(count4))
print("memory address of count4 is", id(count4))

print(F"real value of {count4} ", count4.real)
print(F"imaginary value of {count4} ", count4.imag)


# syntax:
# lambda par1,par2,par3...parn : expression

print("----------------Map---------------")
a = int(input("enter the a number:"))
b = int(input("enter the b number:"))

s = lambda a,b:a*b
print(s(a, b))

cal = lambda c,d:c+d
print(cal('4','5'))

def convert_cols(col):
    return col.lower()
print(convert_cols("ETL TESTING"))

convert_cols_lower = lambda col : col.lower()
print(convert_cols_lower('Sreeni'))

print("----------------Map---------------")
cols= ['Full_Name','First_name','last_name','middle_name', 'Suffix_name','Phone']
print("before conversion", cols)

# map function syntax
# map(function_name, values)

after_conversion = map(convert_cols_lower,cols)
print(list(after_conversion))
#
cols= ['Full_Name','First_name','last_name','middle_name', 'Suffix_name','Phone']

select_name_columns = lambda col : col.lower().endswith('name')
sel = filter(select_name_columns, cols)

print(list(sel))



from functools import *

# ls = [10, 20, 30, 40, 50]
add_two_value = lambda a,b:a+b
print(add_two_value(4,5))

mul_two_value = lambda a,b:a*b
print(mul_two_value(4,5))
ls = [10, 20, 30, 40, 50]
print("sum of all values in ls", sum(ls))
print(reduce(add_two_value,ls))

print(reduce(mul_two_value,ls))

# map -- i/p = o/p - same number values
# filter - o/p <= i/p
# reduce - only one output


ls = [10, 20, 30, 40, 50]
def mul_list_value(ls):
    mul=1
    for i in ls:
        mul = mul *i
    return mul
print("mul value using for loop",mul_list_value(ls))
